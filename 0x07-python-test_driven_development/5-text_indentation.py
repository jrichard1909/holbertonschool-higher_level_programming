#!/usr/bin/python3
"""
    text_indentation
"""


def text_indentation(text):
    """
        prints "text" with 2 newlines
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']

    # Removes the space after special chars
    idx = 0
    for c in text:
        if c in chars:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    # Cats '\n\n' after the special char with removed space
    idx = 0
    for c in text:
        if c in chars:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
