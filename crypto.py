def word_pattern(word):
    word = word.lower() 
    pattern = []
    codes = {}
    code_count = 0

    for char in word:
        if char not in codes:
            codes[char] = code_count
            code_count += 1
        pattern.append(codes[char])

    return ".".join(map(str, pattern))