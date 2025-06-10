def justify(text, width):
    words = text.split()
    justified_text = ""
    line = []
    line_length = 0

    for word in words:
        if line_length + len(word) + len(line) <= width:
            line.append(word)
            line_length += len(word)
        else:
            if len(line) == 1:
                justified_text += line[0] + "\n"
            else:
                spaces_needed = width - line_length
                num_gaps = len(line) - 1
                base_spaces = spaces_needed // num_gaps
                extra_spaces = spaces_needed % num_gaps
                justified_line = ""
                for i, w in enumerate(line):
                    justified_line += w
                    if i < num_gaps:
                        justified_line += " " * base_spaces
                        if i < extra_spaces:
                            justified_line += " "
                justified_text += justified_line + "\n"
            line = [word]
            line_length = len(word)

    if len(line) > 0:
        justified_text += " ".join(line)

    return justified_text
