def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Calculate the factorial of n
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    # Calculate the brazilian factorial
    brazilian_factorial = factorial
    for i in range(n-1, 0, -1):
        brazilian_factorial *= i

    return brazilian_factorial