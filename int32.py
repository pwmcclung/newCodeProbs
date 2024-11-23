def int32_to_ip(int32):
    octets = []
    for i in range(4):
        octet = int32 & 255  
        octets.insert(0, str(octet))  
        int32 >>= 8  
    return ".".join(octets)