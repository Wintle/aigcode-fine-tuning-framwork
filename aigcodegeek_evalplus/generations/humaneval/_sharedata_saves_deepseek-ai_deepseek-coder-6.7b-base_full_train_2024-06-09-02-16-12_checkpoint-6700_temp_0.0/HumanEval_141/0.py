def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts: before and after the dot
    parts = file_name.split('.')
    before_dot, after_dot = parts[0], parts[1]

    # Check if the substring before the dot is not empty and starts with a letter
    if not before_dot or not before_dot[0].isalpha():
        return 'No'

    # Check if there are more than three digits in the file name
    if any(char.isdigit() for char in file_name):
        return 'No'

    # Check if the substring after the dot is one of the allowed values
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'