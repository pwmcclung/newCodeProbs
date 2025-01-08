def ipv4__parser(ip_addr, mask):
    ip_octets = [int(x) for x in ip_addr.split('.')]
    mask_octets = [int(x) for x in mask.split('.')]

    net_octets = []
    host_octets = []

    for i in range(4):
        net_octet = ip_octets[i] & mask_octets[i]
        host_octet = ip_octets[i] & (~mask_octets[i])  

        net_octets.append(net_octet)
        host_octets.append(host_octet)

    net_addr = ".".join(map(str, net_octets))
    host_addr = ".".join(map(str, host_octets))

    return (net_addr, host_addr)