def share_price(invested: float, changes: list[float]) -> str:
    current_value: float = float(invested)  
    for change_percentage in changes:
        multiplier = 1 + (float(change_percentage) / 100.0)
        current_value *= multiplier
    formatted_price = "{:.2f}".format(current_value)
    return formatted_price
