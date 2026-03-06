# 复制WSL中的openclaw.json到Windows桌面（自动适配路径）
cp ~/.openclaw/openclaw.json /mnt/c/Users/Administrator/Desktop/openclaw.json

# 把Windows桌面编辑好的文件复制回WSL的openclaw目录（覆盖原有文件）
cp /mnt/c/Users/Administrator/Desktop/openclaw.json ~/.openclaw/openclaw.json

# 可选：给文件添加正确权限（避免OpenClaw读取权限不足）
chmod 644 ~/.openclaw/openclaw.json

# 查看WSL中最新的配置文件内容（确认是编辑后的版本）
cat ~/.openclaw/openclaw.json

# 取虚拟机IP：
cat /etc/resolv.conf
