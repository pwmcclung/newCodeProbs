def valid_card(card):
    new_card = card.replace(' ', '')
    new_nums = [int(x) for x in new_card]
    last = new_nums[-1]
    others = new_nums[:-1]
    sum = 0
    count = 0
    for x in others:
        if count % 2 == 0:
            num = x * 2
            if num > 9:
                num = num - 9
                sum += num
            else:
                sum += num
        else:
            sum += x
        count +=1
    if (sum + last) % 10 == 0:
        return True
    else:
        return False
