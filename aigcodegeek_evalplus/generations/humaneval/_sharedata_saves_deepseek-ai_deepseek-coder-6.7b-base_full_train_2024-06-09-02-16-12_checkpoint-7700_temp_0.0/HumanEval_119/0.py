def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    s1, s2 = lst
    open_count_s1, close_count_s1 = 0, 0
    open_count_s2, close_count_s2 = 0, 0

    for char in s1:
        if char == '(':
            open_count_s1 += 1
        else:
            close_count_s1 += 1

    for char in s2:
        if char == '(':
            open_count_s2 += 1
        else:
            close_count_s2 += 1

    if open_count_s1 < close_count_s1 and open_count_s2 > close_count_s2:
        return 'Yes'
    elif open_count_s1 > close_count_s1 and open_count_s2 < close_count_s2:
        return 'Yes'
    elif open_count_s1 == close_count_s1 and open_count_s1 == open_count_s2 and close_count_s1 == close_count_s2:
        return 'Yes'
    else:
        return 'No'