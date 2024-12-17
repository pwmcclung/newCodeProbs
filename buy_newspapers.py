def buy_newspaper(s1, s2):
    """
    Calculates the minimum number of newspaper headings needed to obtain s2 from s1.

    Args:
      s1: The heading of a newspaper (string).
      s2: The target word (string).

    Returns:
      The minimum number of newspaper headings needed (integer), or -1 if it's impossible.
    """

    n1 = len(s1)
    n2 = len(s2)

    # 1. Check for impossibility: If any character in s2 is not present in s1, it's impossible to form s2.
    for char in s2:
        if char not in s1:
            return -1

    # 2. Iterate through possible numbers of newspaper headings:
    # We need at least one heading and at most len(s2) headings (in the worst case, each character of s2 comes from a different heading).  We add 1 to account for the edge case where we need exactly n2 headings.
    for num_headings in range(1, n2 + 2): 
        # 3. Concatenate s1 the required number of times:
        combined = s1 * num_headings

        # 4. Check if s2 is a subsequence of the combined string:
        i = 0  # Pointer for the combined string
        j = 0  # Pointer for the target string s2
        while i < len(combined) and j < n2:
            if combined[i] == s2[j]:  # If characters match, move to the next character in s2
                j += 1
            i += 1  # Always move to the next character in the combined string

        # 5. If j reaches the end of s2, it means we found s2 as a subsequence within the combined string.
        if j == n2:
            return num_headings

    # 6. If the loop completes without finding s2, it's impossible to form s2 with the given number of headings.
    return -1