def ipv4_address_class(ipv4_addr):
    first1 = int(ipv4_addr.split('.')[0])
    if (first1) < 128:
        return 'A'
    elif first1 < 192:
          return 'B'
    elif first1 < 224:
        return 'C'
    elif first1 < 240:
        return 'D'
    else:
        return 'E'