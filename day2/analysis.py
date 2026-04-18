from collections import Counter
import re


def smart_text_analyzer(text):
    # Basic Cheractor counting includeing space
    char_count = len(text)

    sentense = [s for s in re.split(r'[.!?]', text) if s.strip()]
    sentence_count = len(sentense)

    words = re.findall(r'\w+', text.lower())
    word_count = len(words)

    word_freq = Counter(words)
    unique_words_count = len(word_freq)
    
    # Get most frequent (returns [('word', count)])
    if words:
        most_frequent_word, freq = word_freq.most_common(1)[0]
    else:
        most_frequent_word, freq = "N/A", 0

    print("📂 --- Text Analysis Report ---")
    print(f"✅ Words: {word_count}")
    print(f"✅ Characters: {char_count}")
    print(f"✅ Sentences: {sentence_count}")
    print(f"✅ Most frequent: '{most_frequent_word}' ({freq} times)")
    print(f"✅ Unique words: {unique_words_count}")
    print("-------------------------------")

input_text = """
AI is the future. AI is revolutionary! 
Learning AI helps you understand machine learning patterns.
"""

smart_text_analyzer(input_text)