def changer(letter, key):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X','Y', 'Z']
    idx_let = letters.index(letter)
    if idx_let != 0:
        new_list = letters[idx_let:] + letters[:idx_let]
    else:
        new_list = letters
    count = 0
    while count != key:
        let = new_list.pop(0)
        new_list.append(let)
        count+=1
    return new_list[0]
    
def caeser(message, key):
    mess_split = list(message.upper())
    new_mess = []
    for x in range(len(mess_split)):
        if mess_split[x].isalpha():
            new_mess.append(changer(mess_split[x], key))
        else:
            new_mess.append(mess_split[x])
    return ''.join(new_mess)
