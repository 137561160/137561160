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
安装好后，不要选ai，直接》
mkdir -p ~/.openclaw
nano ~/.openclaw/openclaw.json
把下面的写进去就可以了。就可以用api了。


{
  "meta": {
    "lastTouchedVersion": "2026.2.1",
    "lastTouchedAt": "2026-02-03T08:20:00.000Z"
  },
  "gateway": {
    "mode": "local",
    "auth": {
      "mode": "token",
      "token": "test123"
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "bailian": {
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "apiKey": "sk-b2e0454555e94c7eaff525f02156d540d",
        "api": "openai-completions",
        "models": [
          {
            "id": "qwen3-max-2026-01-23",
            "name": "qwen3-max-2026-01-23",
            "reasoning": false,
            "input": ["text"],
            "contextWindow": 262144,
            "maxTokens": 65536
          },
          {
            "id": "qwen3-coder-plus",
            "name": "qwen3-coder-plus",
            "reasoning": false,
            "input": ["text"],
            "contextWindow": 131072,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "bailian/qwen3-max-2026-01-23"
      }
    }
  }
}
启动用：openclaw gateway run

网页连接要token: http://127.0.0.1:18789/?token=xxxxxx




