def calculate_time(battery,charger):
    fast_charge = (battery * .85) / charger
    dec_charge = (battery * .10) / (charger * .50)
    trick_charge = (battery * 0.05) / ( charger * 0.20)
    tot_time = round((fast_charge + dec_charge + trick_charge), 2)
    return tot_time