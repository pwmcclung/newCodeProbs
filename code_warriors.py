def get_honor_path(honor_score, target_honor_score):
    if honor_score >= target_honor_score:
        return {}
    points_needed = target_honor_score - honor_score
    kyu_dict = {'2kyus': 0, '1kyus': 0}
    ones = points_needed // 2
    twos = points_needed % 2
    if ones > 0:
        kyu_dict['1kyus'] = ones
    if twos > 0:
        kyu_dict['2kyus'] = 1
    return kyu_dict 