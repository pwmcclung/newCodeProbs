def decode(strng):
    trade_dict = {'0':'5', '1':'9', '2':'8', '3':'7', '4': '6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1'}
    new_string = [trade_dict[x] for x in strng]
    return ''.join(new_string)