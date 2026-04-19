def analyze_text(text):
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text)
    }