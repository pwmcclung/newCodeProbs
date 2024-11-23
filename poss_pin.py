def get_pins(observed):
    nums_per_row = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    
    new_result = ['']
    for item in observed:
        result_list = []
        for obs in new_result:
            for next_item in nums_per_row[item]:
                result_list.append(obs + next_item)
        new_result = result_list
    return new_result