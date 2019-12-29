import sys


# def permutation(string):
#     permutation(string, "")


def permutation(string, prefix):

    if len(string) == 0:
        print(prefix)

    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            permutation(rem, prefix + string[i])

string = "abc"
permutation(string, "")

print(string, "=======")
