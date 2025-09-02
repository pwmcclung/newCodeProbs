def find_squares(num):
    """
    Finds two consecutive perfect squares whose difference is num.

    Args:
      num: An odd integer representing the difference between two consecutive perfect squares.

    Returns:
      A string in the format "bigger-smaller" representing the two squares, 
      or an empty string if no such squares exist.
    """

    # 1. Check for valid input:
    if not (isinstance(num, int) and num > 0 and num < 1000000 and num % 2 != 0):
        return ""  # Return empty string for invalid input

    # 2. Find the smaller square:
    # The difference between consecutive squares is always odd and can be expressed as:
    # (n+1)^2 - n^2 = 2n + 1 = num
    # Solving for n, we get n = (num - 1) // 2
    smaller_num = (num - 1) // 2

    #3. Calculate the two squares:
    smaller_square = smaller_num**2
    bigger_square = (smaller_num + 1)**2

    # 4. Construct and return the formatted string:
    return f"{bigger_square}-{smaller_square}"