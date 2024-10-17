def min_turns(current, target):
    list_current = list(current)
    lst = [int(x) for x in list_current]
    list_target = list(target)
    lst_tar = [int(x) for x in list_target]
    sum_num = 0
    for x in range(len(lst)):
        forPlus = (forwards(lst[x], lst_tar[x]))
        backPlus = (backwards(lst[x], lst_tar[x]))
        sum_num += min(forPlus, backPlus)
    return sum_num
    
def forwards(x,y):
    arr1 = [0,1,2,3,4,5,6,7,8,9]
    arr2 = [0,1,2,3,4,5,6,7,8,9]
    count1 = 0
    while arr1.index(x) != arr2.index(y):
        first = arr1.pop(0)
        arr1.append(first)
        count1 += 1
    return count1
        
    

def backwards(x,y):
    arr1 = [0,1,2,3,4,5,6,7,8,9]
    arr2 = [0,1,2,3,4,5,6,7,8,9]
    count2 = 0
    while arr1.index(x) != arr2.index(y):
        first = arr1.pop()
        arr1.insert(0,first)
        count2 += 1  
    return count2