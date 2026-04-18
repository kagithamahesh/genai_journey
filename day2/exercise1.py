def text_analyzer(msg):
    freq={}
    for word in msg.lower().split():
      freq[word] = freq.get(word,0)+1

    print(freq)

text_analyzer("hello world hello")


# text = "Apple apple APPLE Orange orange"
# words = text.lower().split()
# word_freq = {}

# for word in words:
#     # Get current count, defaulting to 0 if the word isn't in the dict
#     word_freq[word] = word_freq.get(word, 0) + 1

# print(word_freq)
