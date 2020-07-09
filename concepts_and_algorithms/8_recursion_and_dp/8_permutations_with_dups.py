def print_perms(string: str):
    result = []
    char_frequency = build_frequency_table(string)
    _print_perms(char_frequency, "", len(string), result)
    return result

def build_frequency_table(string: str):
    char_frequency = {}
    for c in string:
        if c not in char_frequency:
            char_frequency[c] = 1
        else:
            char_frequency[c] += 1
    
    return char_frequency

def _print_perms(char_frequency: dict, prefix: str, remaining: int, result: list):
    if remaining == 0:
        result.append(prefix)
        return
    
    for c, count in char_frequency.items():
        if count > 0:
            char_frequency[c] -= 1
            _print_perms(char_frequency, prefix + c, remaining - 1, result)
            char_frequency[c] = count

print(print_perms("aabbcc"))
