def get_permutations(string: str):
    if len(string) == 0: 
        return [""]

    perms = get_permutations(string[:-1])
    new_perms = []
    for word in perms:
        for i in range(len(word) + 1):
            new_perm = word[:i] + string[-1] + word[i:]
            new_perms.append(new_perm)
    return new_perms

print(get_permutations("abcd"))

def permutations_using_prefix(string: str):
    result = []
    _permutations_using_prefix("", string, result)
    return result

def _permutations_using_prefix(prefix: str, remainder: str, result: list):
    if len(remainder) == 0: result.append(prefix)

    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1:]
        c = remainder[i]
        _permutations_using_prefix(prefix + c, before + after, result)


print(permutations_using_prefix("abc"))


def get_perms(remainder: str):
    length = len(remainder)
    result = []
    if length == 0:
        result.append("")
        return result
    
    for i in range(length):
        before = remainder[0: i]
        after = remainder[i + 1:]

        partials = get_perms(before + after)

        for word in partials:
            result.append(remainder[i] + word)
        
    return result

print(get_perms("abd"))