def reverse_invert(lst):
    result = []
    for item in lst:
        if isinstance(item, int):
            item_str = str(abs(item))  
            reversed_item_str = item_str[::-1]  
            reversed_item = int(reversed_item_str)  
            
            if item >= 0:
                result.append(-reversed_item) 
            else:
                result.append(reversed_item)  

    return result