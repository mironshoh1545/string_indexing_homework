def nu(s):
    if s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9' or s =='0':
        return 1
    return 0

def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    answer = nu(s[0]) + nu(s[1]) + nu(s[2]) + nu(s[3]) + nu(s[4])
    return answer