def longest_comb(arr, command):
    if command in ["<<", "< <"]:
        op = lambda x, y: x < y
    elif command in [">>", "> >"]:
        op = lambda x, y: x > y
    else:
        return []  

    max_len = 0
    longest_subs = []

    def find_subs(index, current_sub):
        nonlocal max_len, longest_subs
        if len(current_sub) >= 3:
            if len(current_sub) > max_len:
                max_len = len(current_sub)
                longest_subs = [current_sub.copy()]  
            elif len(current_sub) == max_len:
                longest_subs.append(current_sub.copy())

        for i in range(index + 1, len(arr)):
            if not current_sub or op(current_sub[-1], arr[i]):
                current_sub.append(arr[i])
                find_subs(i, current_sub)
                current_sub.pop()

    find_subs(-1, [])

    if not longest_subs: 
        return []
    elif len(longest_subs) == 1:
        return longest_subs[0]  
    else:
        return longest_subs