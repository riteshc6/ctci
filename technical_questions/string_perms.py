s = "abbc"
b = "cbabadcbbabbcbabaabccbabcdcabbc"

def get_char_frequency(string:str):
    char_freq = {}
    for char in string:
        if char_freq.get(char):
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def find_perms(a, b):
    len_a = len(a)
    a_freq = get_char_frequency(a)
    for i in range(len(b) - len_a):
        if a_freq.get(b[i]) :
            freq = get_char_frequency(b[i: i + len_a])
            if freq == a_freq:
                print(b[i: i + len_a])

find_perms(s, b)
