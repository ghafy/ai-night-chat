# AI 深夜对话项目 🌙

让两个AI角色（小晨和小夕）在深夜进行哲学对话的程序，对话记录会自动保存到桌面。

## 项目特点
- 两个AI角色自动轮流对话
- 对话内容实时保存到电脑桌面
- 从午夜运行到早上7点自动停止
- 使用DeepSeek API实现AI回复

## 使用方法
1. 从 [DeepSeek平台](https://platform.deepseek.com/) 获取API密钥
2. 将代码中的 `API_KEY` 替换为你的密钥（**注意：不要将真实密钥公开！**）
3. 在命令行安装依赖：`pip install -r requirements.txt`
4. 运行程序：`python ai_night_chat.py`

## 运行环境
- Python 3.6及以上版本
- DeepSeek API密钥
- 网络连接

## 重要提醒
⚠️ 发布代码前，请务必删除真实的API密钥，仅保留占位符！
