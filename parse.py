def parse_html_color(color):
    color = color.lower()
    if color in PRESET_COLORS:
        hex_color = PRESET_COLORS[color]
        return parse_hex_color(hex_color)
    elif color.startswith('#'):
        return parse_hex_color(color)
    else:
        return None

def parse_hex_color(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        r = int(hex_color[0] * 2, 16)
        g = int(hex_color[1] * 2, 16)
        b = int(hex_color[2] * 2, 16)
    elif len(hex_color) == 6:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    else:
        return None 

    return {'r': r, 'g': g, 'b': b}