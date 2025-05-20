def is_cyrillic(letter):
    if '\u0400' <= letter and letter <= '\u04FF':
        return True
    else:
        return False
