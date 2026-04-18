def analyze_text(msg):
    word = msg.split()

    num_word = len(word)
    num_char = len(msg)
    return{
            "words":num_word,
            "characters":num_char
    }

text = input("Enter a paragraph: ")

result = analyze_text(text)
print("Word count:", result["words"])
print("Character count:", result["characters"])