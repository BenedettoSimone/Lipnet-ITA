def text_to_labels(text):
    ret = []
    for char in text:
        if char.lower() >= 'a' and char.lower() <= 'z':
            ret.append(ord(char.lower()) - ord('a'))
        elif char == ' ':
            ret.append(26)
    return ret

def labels_to_text(labels):
    # 26 is space, 27 is CTC blank char
    text = ''
    for c in labels:
        if c >= 0 and c < 26:
            text += chr(c + ord('a'))
        elif c == 26:
            text += ' '
    return text


