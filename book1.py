def amount_of_pages(summary):
    n = 0
    digits_counted = 0
    power_of_10 = 1
    num_digits = 1

    while digits_counted < summary:
        upper_bound = min(power_of_10 * 10 -1, 10**6) 


        pages_in_range = upper_bound - power_of_10 +1


        digits_in_range = pages_in_range * num_digits

        if digits_counted + digits_in_range <= summary:
            digits_counted += digits_in_range
            n += pages_in_range
            power_of_10 *= 10
            num_digits += 1

        else: 
            remaining_digits = summary - digits_counted
            remaining_pages = remaining_digits // num_digits
            n += remaining_pages
            digits_counted += remaining_pages * num_digits
            break


    return n