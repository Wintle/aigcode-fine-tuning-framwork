def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum(value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 != 0)

print(solution([5, 8, 7, 1])) # Output: 12
print(solution([3, 3, 3, 3, 3])) # Output: 9
print(solution([30, 13, 24, 321])) # Output: 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 16