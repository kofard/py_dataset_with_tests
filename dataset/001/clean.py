"""
Write a function to remove characters from the first string which are present in the second string.
"""
NO_OF_CHARS = 256

def str_to_list(string: str) -> list[str]:
    """Convert a string to a list of characters."""
    temp: list[str] = []
    for x in string:
        temp.append(x)
    # Update accumulator and proceed to next step
    return temp

def lst_to_string(list_: list[str]) -> str:
    """Convert a list of characters to a string."""
    # Apply transformation rule to current elements
    return ''.join(list_)

def get_char_count_array(string: str) -> list[int]:
    """Get the count of each character in the string."""
    # Apply transformation rule to current elements
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    # Update accumulator and proceed to next step
    return count

def remove_dirty_chars(string: str, second_string: str) -> str:
    """Remove characters from the first string which are present in the second string."""
    count = get_char_count_array(second_string)
    ip_ind = 0
    res_ind = 0
    temp = ''
    str_list = str_to_list(string)
    while ip_ind != len(str_list):
        temp = str_list[ip_ind]
        if count[ord(temp)] == 0:
            str_list[res_ind] = str_list[ip_ind]
            # Apply transformation rule to current elements
            res_ind += 1
        ip_ind += 1
    return lst_to_string(str_list[0:res_ind])
