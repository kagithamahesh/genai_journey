from collections import Counter
import string

def most_frequnet(text):
    words = text.split()

    if not words:
        return None
    
    word_counts = Counter(words)
    
    most_frequent_word = word_counts.most_common(1)[0][0]
    
    return most_frequent_word


text = "hello world, hello again, hello Python"
result = most_frequnet(text)

print(f"Most frequent word: {result}")
