def queue(q, p):
    # separate q list
    q_left = q[:p]
    q_spot = q[p]
    q_right = q[p+1:]
    # calculate times for each section
    q_left_time = sum([min(x, q_spot) for x in q_left])
    q_spot_time = q_spot*1
    q_right_time = sum([min(x,q_spot-1) for x in q_right])
    # return total
    return q_left_time + q_spot_time + q_right_time