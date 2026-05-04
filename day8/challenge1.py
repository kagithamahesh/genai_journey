def total_tokens(messages):
    return sum(message["tokens"] for message in messages)


def trim_to_budget(messages, token_budget):
    if not messages:
        return []

    trimmed = []
    start_index = 0

    # Keep first system message if present
    if messages[0]["role"] == "system":
        trimmed.append(messages[0])
        start_index = 1

    current_tokens = total_tokens(trimmed)
    selected = []

    # Add most recent messages first
    for msg in reversed(messages[start_index:]):
        if current_tokens + msg["tokens"] <= token_budget:
            selected.append(msg)
            current_tokens += msg["tokens"]

    trimmed.extend(reversed(selected))
    return trimmed


def add_message(messages, role, content, token_budget=50):
    # Estimate token count
    tokens = len(content.split())

    # Append new message
    messages.append({
        "role": role,
        "content": content,
        "tokens": tokens
    })

    # Trim automatically to budget
    return trim_to_budget(messages, token_budget)


# Example usage
messages = [
    {"role": "system", "content": "You are a helpful assistant.", "tokens": 5},
]

messages = add_message(messages, "user", "What is machine learning?")
messages = add_message(messages, "assistant", "Machine learning allows systems to learn from data.")

print(messages)
print("Total tokens:", total_tokens(messages))