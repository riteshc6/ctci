from typing import List

def gen_parens(remaining: int):
    parens = set()
    if remaining == 0:
        parens.add("")
    
    else:
        prev = gen_parens(remaining - 1)
        for string in prev:
            for i in range(len(string)):
                if string[i] == "(":
                    s = string[0: i + 1] + "()" + string[i + 1:]
                    parens.add(s)
            parens.add("()" + string)
    return parens

print(gen_parens(3))


def add_paren(parens_list: List[str], left_rem: int, right_rem: int, string_list: List[str], count: int):
    if left_rem < 0 or right_rem < left_rem:
        return
    
    if left_rem == 0 and right_rem == 0:
        string = "".join(string_list)
        parens_list.append(string)
    else:
        if left_rem > 0:
            string_list[count] = "("
            add_paren(parens_list, left_rem - 1, right_rem, string_list, count + 1)
        
        if right_rem > left_rem:
            string_list[count] = ")"
            add_paren(parens_list, left_rem, right_rem - 1, string_list, count + 1)

def generate_parens(count: int):
    string_list = [0] * count * 2
    parens_list = []
    add_paren(parens_list, count, count, string_list, 0)
    return parens_list

print(generate_parens(3))
