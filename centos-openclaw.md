第一步：系统更新与基础依赖安装
首先更新系统并安装编译工具和基础库。
bash

编辑



# 更新系统
sudo dnf update -y

# 安装基础开发工具、Git、Python3、NodeJS源所需工具
sudo dnf install -y git curl vim gcc gcc-c++ make python3 python3-pip python3-devel openssl-devel bzip2-devel libffi-devel zlib-devel
第二步：安装 Node.js (版本必须 ≥ 20)
OpenClaw 需要较新的 Node.js 版本。Alibaba Cloud Linux 3 默认源里的 Node.js 版本可能过老，我们使用 NodeSource 源安装 Node.js 20 LTS。
bash

编辑



# 1. 清理旧版本 (如果有)
sudo dnf remove -y nodejs npm

# 2. 添加 Node.js 20.x 源
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -

# 3. 安装 Node.js 和 npm
sudo dnf install -y nodejs

# 4. 验证版本 (确保 Node v20+, npm v9+)
node -v
npm -v


第一步：下载并运行安装脚本
bash

编辑



curl -fsSL https://openclaw.ai/install.sh | bash
这个脚本会自动检测环境、安装 Node.js (如果需要)、安装 OpenClaw 全局包。
注意观察：如果脚本执行过程中再次出现 JavaScript heap out of memory，请立刻告诉我。
第二步：如果安装成功，配置内存环境变量
安装完成后，为了确保运行时不崩溃，立刻执行这句（将其写入配置文件，永久生效）：
bash

编辑



echo 'export NODE_OPTIONS="--max-old-space-size=1200"' >> ~/.bashrc && source ~/.bashrc
第三步：启动
bash

编辑



openclaw onboard
(如果 onboard 依然卡住，我们就用上次说的“手动创建 config.json”的方法，那个最稳)
