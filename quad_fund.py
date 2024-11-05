import math
def qf(donations: list, pool: int) -> list:
    don_list = [int(fundingCalc(x)) for x in donations]
    sum_don_list = sum(don_list)
    new_list = [round(pool * x/sum_don_list) for x in don_list]
    return new_list
    
def fundingCalc(don):
    sum = 0
    for x in don:
        sum += math.sqrt(x)
    return sum**2