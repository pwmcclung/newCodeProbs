def get_section_id(scroll, sizes):
    start = -1
    section = 0
    while len(sizes) > 0:
        first = sizes.pop(0)
        start += first
        if scroll <= start:
            return section
        else:
            section += 1
    return -1
