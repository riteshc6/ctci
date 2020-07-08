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
