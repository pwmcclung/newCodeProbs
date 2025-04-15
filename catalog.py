import re

def catalog(s, article):
    lines = s.strip().split('\n\n')
    result = []
    for line in lines:
        match = re.search(r'<prod><name>(.*?)</name><prx>(.*?)</prx><qty>(.*?)</qty></prod>', line)
        if match:
            name = match.group(1)
            price = match.group(2)
            qty = match.group(3)
            if article in name:
                result.append(f"{name} > prx: ${price} qty: {qty}")
    if result:
        return "\r\n".join(result) 
    else:
        return "Nothing"
