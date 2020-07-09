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
