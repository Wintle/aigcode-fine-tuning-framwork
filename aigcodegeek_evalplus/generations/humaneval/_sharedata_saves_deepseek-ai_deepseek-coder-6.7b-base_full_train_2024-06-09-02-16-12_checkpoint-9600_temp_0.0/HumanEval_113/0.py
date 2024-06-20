def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    output = []
    for i, s in enumerate(lst):
        odd_digits = sum(1 for c in s if int(c) % 2 != 0)
        output.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odd_digits, odd_digits, i+1, i+1))
    return output