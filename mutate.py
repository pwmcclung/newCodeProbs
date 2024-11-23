def contamination(text, char):
    if text == '':
        return ''
    else:
        length = len(text)
        return char * length