def greet(name):
    return f"Hello,{name}"


print(greet("hai"))

def double(val):
    return val * 2

print(double(5))

def describe_model(name,tokens):
    return f"{name} can handle {tokens} tokens"

print(describe_model("claude", 8192))