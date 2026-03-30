def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    symbols = ".,!?-;:()"
    for symbol in symbols:
        s = s.replace(symbol, "")
    return s == s[::-1]
