def detect_language(text): # automatic language detection.

    for ch in text:

        if '\u0600' <= ch <= '\u06FF':
            return "fa"

    return "en"