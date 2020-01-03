s = "xyz"

def perm(string):
    length_s  = len(string)
    if length_s == 1:
        return [string]

    perm_s = perm(string[0:length_s - 1])
    perms = []
    nth_char = string[-1]
    for word in perm_s:
        for i in range(len(word) + 1):
            new_word = word[:i] + nth_char + word[i:]
            perms.append(new_word)
    return perms   

perm("abc")