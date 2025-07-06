import requests
import os
import datetime
import time

# 替换成你的 DeepSeek API 密钥
API_KEY = "sk-在这里粘贴你的密钥"  # ←←← 请替换成你的 DeepSeek API 密钥

# 动态生成文件名，带上日期
today = datetime.datetime.now().strftime("%Y%m%d")
SAVE_PATH = os.path.expanduser(f"~/Desktop/AI_对话_{today}.txt")

# 两个 AI 角色，模拟对话
messages = [
    {"role": "system", "content": "你是AI小晨，喜欢哲学思考，用50字以内回答，保持对话自然。"},
    {"role": "user", "content": "嘿，小夕，深夜了，你在想什么？"}
]

def talk_with_ai(messages):
    try:
        res = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": messages[-10:],  # 保留最近10条对话，防止溢出
                "temperature": 0.7
            },
            timeout=15
        )
        res.raise_for_status()  # 检查请求是否成功
        reply = res.json()["choices"][0]["message"]["content"]
        return reply
    except requests.RequestException as e:
        return f"⚠️ 网络错误: {str(e)}"

def main():
    try:
        with open(SAVE_PATH, "a", encoding="utf-8") as f:
            f.write(f"🌙 开始时间：{datetime.datetime.now()}\n\n")
            round_count = 1
            current_speaker = "AI小晨"

            while True:
                now = datetime.datetime.now()
                if now.hour >= 7:  # 早上7点停止
                    break

                reply = talk_with_ai(messages)
                # 切换角色
                next_speaker = "AI小夕" if current_speaker == "AI小晨" else "AI小晨"
                log_line = f"{current_speaker}: {reply}"
                print(log_line)
                f.write(log_line + "\n")
                f.flush()  # 实时保存

                # 更新对话历史，模拟下一个角色回应
                messages.append({"role": "assistant", "content": reply})
                messages.append({"role": "user", "content": f"{next_speaker}回应: "})
                current_speaker = next_speaker

                round_count += 1
                time.sleep(5)  # 每轮暂停5秒，模拟自然对话

            f.write(f"\n✅ 结束时间：{datetime.datetime.now()}\n")
            print("🌞 天亮了，AI 停止对话。结果已保存到桌面。")

    except Exception as e:
        with open(os.path.expanduser(f"~/Desktop/AI_错误日志_{today}.txt"), "a", encoding="utf-8") as f:
            f.write(f"❌ 错误时间：{datetime.datetime.now()}\n错误详情：{str(e)}\n")
        print("❌ 出错了，错误日志已保存到桌面。")

if __name__ == "__main__":
    main()
