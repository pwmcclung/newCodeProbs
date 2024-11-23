import re
def evenator(s):
    text = re.sub(r"[.,?!_]", "", s)

    words = text.split()
    translated = []

    for w in words:
        if len(w) % 2 != 0: 
            w += w[-1]  
        translated.append(w)

    return " ".join(translated)