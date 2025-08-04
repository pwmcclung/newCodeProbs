def get_participants(handshakes):
    if handshakes == 0:
        return 0

    n = 0
    while n * (n - 1) // 2 < handshakes:
        n += 1
    return n