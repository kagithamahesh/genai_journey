dataset = [
    {"input": "Translate to French: Hello",  "output": "Bonjour"},
     {"input": "Translate to French: Goodbye", "output": "Au revoir"},
    {"input": "Translate to French: Thank you","output": "Merci"},
]

prompts = [ row["input"] for row in dataset]
labels=[row["output"]for row in dataset]

short_examples = [row for row in dataset if len(row["input"]) < 35]