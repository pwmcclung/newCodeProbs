def cog_RPM(cogs):
    if not cogs:
        return 0
    rpm = 1.0
    for i in range(len(cogs) -1):
        rpm = rpm * (-cogs[i] / cogs[i+1])
    return rpm