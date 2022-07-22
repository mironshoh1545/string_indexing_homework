def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0] == '*' :
        return 0
    elif s[1] == '*':
        return 1
    elif s[2] == '*':
        return 2
    elif s[3] == '*':
        return 3
    elif s[4] == '*':
        return 4
    return False