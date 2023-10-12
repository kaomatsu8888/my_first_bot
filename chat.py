def chat_completion(user_content):
    # ここで問い合わせフォームへのリンクを返す
    reply_message = "問い合わせはこちらのフォームからお願いします: [リンク]"
    return reply_message

def main():
    user_content = "Hello!"
    reply_message = chat_completion(user_content)
    print(reply_message)

if __name__ == "__main__":
    main()