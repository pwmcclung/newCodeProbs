def palindrome(s):
    s = s.lower()
    list_s = list(s)
    consonants = list('bcdfghjklmnpqrstvwxyz')
    vowels = list('aeiou')
    cons = [x for x in list_s if x in consonants]
    vows = [x for x in list_s if x in vowels]
    cons_joined = ''.join(cons)
    vows_joined = ''.join(vows)
    cons_rev = cons_joined[::-1]
    vows_rev = vows_joined[::-1]
    if cons_joined == cons_rev and vows_joined == vows_rev:
        return 'both'
    elif cons_joined == cons_rev and vows_joined != vows_rev:
        return 'consonant'
    elif cons_joined != cons_rev and vows_joined == vows_rev:
        return 'vowel'
    else:
        return 'neither'