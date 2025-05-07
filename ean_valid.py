def validate_ean(code):
    num_code = [int(x) for x in code]
    last = num_code[-1]
    first_part = num_code[0:-1]
    sum = 0
    count = 0
    for x in range(len(first_part)):
        if count % 2 != 0:
            sum += first_part[x] * 3
        else:
            sum += first_part[x] * 1
        count+=1
    if sum % 10 == 0 and last == 0:
        return True
    if sum % 10 == 0 and last != 0:
        return False
    if sum % 10 != 0:
        if 10 - (sum % 10) == last:
            return True
        else:
            return False
