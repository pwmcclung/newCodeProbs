def assistance(weight):
    locks_weight = 5
    available_disks = {
        "red": 25,
        "blue": 20,
        "yellow": 15,
        "green": 10,
        "black": 5,
        "orange": 2.5,
        "white": 1.25,
    }

    if weight < 20:
        return "Error" 
    if weight == 20: 
        return "Nothing to hang"
    if weight < 25 and weight > 20:
        return 'Error'
    if weight == 25:
        return 'Only lock'
    disks = {}
    remaining_weight = (weight - 25) / 2

    for disk_name, disk_weight in sorted(available_disks.items(), key=lambda item: item[1], reverse=True):
      while remaining_weight >= disk_weight:
        remaining_weight -= disk_weight
        disks[disk_name] = disks.get(disk_name, 0) + 1
    
    if remaining_weight > 0:
        return "Error"

    result = []
    for disk_name, count in disks.items():
        result.append(f"{count} {disk_name + ('s' if count > 1 else '')}")
    
    result.append("lock")
    return ", ".join(result)