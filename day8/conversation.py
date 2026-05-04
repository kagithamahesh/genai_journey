conversation = [
    {
        "role": "system",
        "content": "You are a helpful data science tutor."
    },
    {
        "role": "user",
        "content": "What is gradient descent?"
    },
    {
        "role": "assistant",
        "content": "Gradient descent is an optimization algorithm..."
    }
]

#add a new user message(list append +dict literal)
def add_message(histor:list,role:str,content:str)->list:
    histor.append({"role":role,"content":content})
    return histor


print(add_message(conversation,"user","Can you give me an example?"))

