chat = []

def add_message(chat,role,txt):
    message={"role":role,"content":txt}

    chat.append(message)
    return chat


chat = add_message(chat, "user","What is AI?")
chat = add_message(chat, "assistant", "AI is machines that learn.")
chat = add_message(chat, "user",      "Give an example.")
chat = add_message(chat,"assistant","'For example, a spam filter.'")


for msg in chat:
    print(f"{msg['role']} :{msg['content']}")


def last_message(chat):
    return chat[-1]['content'] ,chat[-1]['role'] 
print(last_message(chat))   