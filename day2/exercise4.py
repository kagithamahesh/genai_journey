def analyze_txt(text):
    words = text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word,0)+1

    
    return freq
    # num_words = len(words)
    # num_char = len(text)

    # return {
    #     "characters" : num_char,
    #     "words" : num_words
    # }

text = input("Enter a paragraph: ")

result = analyze_txt(text)

print(result)

# print("Word count:", result["words"])
# print("Character count:", result["characters"])