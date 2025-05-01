def is_planet_mnemonic_correct(solar_system, mnemonic):
    s = sorted([x[0] for x in solar_system if x != 'Asteroid'])
    m = sorted([x[0] for x in mnemonic.split()])
    if s == m:
        return True
    else:
        return False
