def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    znaki = ".,!?-;:()"
    for znak in znaki:
        s = s.replace(znak, "")
    return s == s[::-1]