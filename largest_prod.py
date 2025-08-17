def greatest_product(st):
    str_nums = [int(x) for x in st]
    arr = []
    while len(str_nums) >4:
        arr.append(str_nums[0] * str_nums[1] * str_nums[2] * str_nums[3] * str_nums[4])
        str_nums.pop(0)
    return max(arr)