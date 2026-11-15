def min_window(search_str: str, target_letters: str) -> str:
    """Given a string to search, and another string of target char_dict,
    return the smallest substring of the search string that contains
    all target char_dict.

    This is somewhat modified from my solution to the problem
    "Minimum Window Substring" on leetcode.
    https://leetcode.com/problems/minimum-window-substring/description/"""
    target_count = len(target_letters)
    search_len = len(search_str)
    if search_len < target_count:
        return ''
    char_dict = {}
    for ch in target_letters:
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    window_start = 0
    window_end = 0
    exists = False
    min_window_len = search_len + 1
    while window_end < search_len:
        while target_count > 0 and window_end < search_len:
            cur = search_str[window_end]
            if cur in char_dict:
                char_dict[cur] -= 1
                if char_dict[cur] >= 0:
                    target_count -= 1
            window_end += 1
        temp = window_end - window_start
        if target_count == 0 and temp < min_window_len:
            min_window = [window_start, window_end]
            exists = True
            min_window_len = temp
        while target_count == 0 and window_start < window_end:
            cur = search_str[window_start]
            window_start += 1
            if cur in char_dict:
                char_dict[cur] += 1
                if char_dict[cur] > 0:
                    break
        temp = window_end - window_start + 1
        if temp < min_window_len and target_count == 0:
            min_window = [window_start - 1, window_end]
            min_window_len = temp
        target_count = 1
    if exists:
        return search_str[min_window[0]:min_window[1]]
    else:
        return ''