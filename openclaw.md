install steps for openclaw in China:
1.install ubuntu to windows, as I don't want C disc is too much, I am trying to install in D:
problem:
install WSL2 to D:
# 开启 WSL 和虚拟机平台功能
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 设置 WSL2 为默认版本
wsl --set-default-version 2

# 安装 Ubuntu（默认是最新版，也可以指定版本如 Ubuntu-22.04）直接安装不了的。改为下载先
[wsl --install -d Ubuntu ]
$url = "https://aka.ms/wslubuntu2204"
$output = "$env:USERPROFILE\Desktop\Ubuntu2204.msixbundle"
Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing

# 3. 检查文件完整性（确保下载未中断）
Get-Item $output | Format-List Name, Length
Add-AppxPackage -Path "$env:USERPROFILE\Desktop\Ubuntu2204.msixbundle" -ForceApplicationShutdown

# 安装内置版 WSL，不通过 Microsoft Store
wsl --install --inbox --no-distribution

# 安装 Ubuntu 分发版--这里才能安装
wsl --install -d Ubuntu

PS C:\Users\Administrator> wsl --install -d Ubuntu
Ubuntu 已安装。
正在启动 Ubuntu…
PS C:\Users\Administrator> wsl --shutdown
PS C:\Users\Administrator> wsl --export Ubuntu D:\WSL\ubuntu_backup.tar
PS C:\Users\Administrator> wsl --unregister Ubuntu
正在注销...
PS C:\Users\Administrator> # 核心导入命令
PS C:\Users\Administrator> wsl --import Ubuntu-22.04 D:\WSL\Ubuntu D:\Ubuntu_backup\ubuntu_backup.tar --version 2
系统找不到指定的路径。
PS C:\Users\Administrator> wsl --import Ubuntu D:\WSL\Ubuntu D:\WSL\ubuntu_backup.tar --version 2
WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel

# 下载 WSL2 内核更新包到临时文件夹
Invoke-WebRequest -Uri https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile $env:TEMP\wsl_update_x64.msi

# 静默安装内核更新包（无需手动点击下一步）
Start-Process msiexec.exe -ArgumentList "/i $env:TEMP\wsl_update_x64.msi /qn /norestart" -Wait

# 验证安装并设置 WSL2 为默认版本
wsl --set-default-version 2

# 1. 检查备份文件是否存在（验证路径）
Get-ChildItem D:\WSL\ubuntu_backup.tar

# 2. 确保目标安装目录存在（不存在则创建）
New-Item -Path D:\WSL\Ubuntu -ItemType Directory -Force

# 3. 执行导入命令（指定 WSL2 版本）
wsl --import Ubuntu D:\WSL\Ubuntu D:\WSL\ubuntu_backup.tar --version 2

# 1. 查看已导入的 WSL 分发版
wsl -l -v

# 2. 启动导入的 Ubuntu
wsl -d Ubuntu

# 先进入 Ubuntu 系统
wsl -d Ubuntu-22.04
# 在 Ubuntu 终端中执行（替换为你的用户名，比如 ubuntu）
echo "你的用户名 ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/你的用户名
sudo sed -i 's/root/你的用户名/' /etc/passwd
# 退出 Ubuntu
exit
# （可选）设置该 Ubuntu 为默认 WSL 发行版
wsl --set-default Ubuntu-22.04 
-------------------------------------------------------------------------------------------------------------------------------------
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw --version
openclaw onboard
# 后面直接quick start, 选模型那里就用qwen

# 核心启动命令：直接运行 gateway 模块，自动绑定默认端口 18789
openclaw gateway

# 打开后的连接
http://127.0.0.1:18789/chat?session=main

----------------------------------------------------------------------------------------------------------------
# 后台启动网关（输出日志到文件，方便查看）
nohup openclaw gateway start > ~/openclaw.log 2>&1 &

# 查看后台进程
ps aux | grep openclaw

openclaw gateway stop

--------------------------------------------------------------------------------------
二、核心方案：自定义代理转发-------------API 
cat > ~/aliyun-proxy.js << EOF
const http = require('http');
const https = require('https');
const url = require('url');

// 你的有效阿里云 API Key
const API_KEY = 'sk-88d28af8d11a487XXX3251725f6e';
// 阿里云百炼兼容接口
const TARGET_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1';

// 创建代理服务器
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const targetPath = parsedUrl.pathname;
  const targetFullUrl = TARGET_URL + targetPath;

  // 构建转发请求
  const options = url.parse(targetFullUrl);
  options.method = req.method;
  options.headers = {
    ...req.headers,
    'Authorization': \`Bearer \${API_KEY}\`,
    'Content-Type': 'application/json',
    'Host': 'dashscope.aliyuncs.com'
  };

  // 转发请求到阿里云
  const proxyReq = https.request(options, (proxyRes) => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res);
  });

  // 处理请求体
  req.pipe(proxyReq);

  // 错误处理
  proxyReq.on('error', (err) => {
    res.writeHead(500);
    res.end(JSON.stringify({ error: err.message }));
  });
});

// 代理服务器监听 3000 端口
server.listen(3000, '0.0.0.0', () => {
  console.log('阿里云百炼代理服务器启动：http://127.0.0.1:3000');
});
EOF

步骤 2：启动代理服务器
bash
运行
# 启动代理（保持这个终端打开）
node ~/aliyun-proxy.js

步骤 3：配置 OpenClaw 指向本地代理
bash
运行
# 1. 设置 qwen 节点指向本地代理
openclaw config set models.providers.qwen.baseUrl "http://127.0.0.1:3000"
openclaw config set models.providers.qwen.apiKey "dummy-key"  # 代理会覆盖，随便填
openclaw config set agents.defaults.model.primary "qwen/qwen-turbo"

# 2. 禁用 qwen-portal 插件
openclaw config set plugins.entries.qwen-portal-auth.enabled false

# 新开终端，启动 Gateway
openclaw gateway

# 再新开终端，调用模型（必成功）
openclaw agent --agent main --message "你好，测试阿里云百炼模型"


终端 1：只启动代理服务器（核心，必须保持运行）
bash
运行
# 执行这行命令后，终端会显示 "阿里云百炼代理服务器启动：http://127.0.0.1:3000"
# ✅ 不要按任何键、不要关闭这个终端！
node ~/aliyun-proxy.js

终端 2：只启动 Gateway（忽略 UI 警告）
bash
运行
# 先杀旧进程，再启动 Gateway
pkill -9 -f "openclaw gateway"
openclaw gateway

方案 2：获取原始 token（如需保留认证）
如果想保留 token 认证，执行以下命令查看未脱敏的 token：
bash
运行
# 直接读取配置文件，获取原始 token
cat ~/.openclaw/openclaw.json | grep -E '"token":\s*"[^"]+"'

复制这串 abcdef1234567890xyz...，然后打开带 token 的链接：
plaintext
http://127.0.0.1:18789/#token=abcdef1234567890xyz...



