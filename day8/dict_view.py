model_config = {
    "name": "claude-sonnet",
    "max_tokens": 8192,
    "temperature": 0.7,
    "supports_vision": True
}

# print(model_config.get("timeout",30))

# Modify
model_config["temperature"] = 0.3
model_config["top_p"] = 0.9

# print(model_config)
for key,val in model_config.items():
    print(f"{key}:{val}")