def build_or_buy(hand):
    lst = []
    hand_cop = hand[:]
    if hand_cop.count('b') >= 1 and hand_cop.count('w') >= 1:
        lst.append('road')
    if hand_cop.count('b') >= 1 and hand_cop.count('w') >= 1 and hand_cop.count('s') >= 1 and hand_cop.count('g') >= 1:
        lst.append('settlement')
    if hand_cop.count('o') >= 3 and hand_cop.count('g') >= 2:
        lst.append('city')
    if hand_cop.count('o') >= 1 and hand_cop.count('s') >= 1 and hand_cop.count('g') >= 1:
        lst.append('development')
    return lst