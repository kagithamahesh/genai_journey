names=["Alice", "Bob", "Carol"]

for name in names:
    print(name)


for name in names:
    print(f"hello, {name}")

scores = {"math": 90, "english": 80, "science": 95}

for subject,score in scores.items():
    print(f"{subject}: {score}")