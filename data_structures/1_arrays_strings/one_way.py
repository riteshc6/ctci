import unittest

def one_way(strA, strB):

    len_A = len(strA)
    len_B = len(strB)
    edit_ops = 0

    if abs(len_A - len_B) > 1:
        return False

    if len_A == len_B:
        for charA, charB in zip(strA, strB):
            if charA != charB:
                edit_ops += 1
                if edit_ops > 1:
                    return False
        return True

    elif len_A > len_B:

        idx = 0

        for char in strB:
            if strA[idx] != char:
                strA = strA[:idx] + strA[idx + 1:]
                break
            idx += 1
        else:
            strA = strA[:-1]

        return strA == strB


    elif len_A < len_B:
        idx = 0

        for char in strA:
            if strB[idx] != char:
                strA = strA[:idx] + strB[idx] + strA[idx:]
                break
            else:
                idx += 1
        else:
            strA += strB[-1]
        return strA == strB



class Test(unittest.TestCase):

    def test_one_way(self):

        data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

        for strA, strB, expected in data:
            print(strA, strB)
            actual = one_way(strA, strB)
            self.assertEqual(actual, expected)
            


if __name__ == "__main__":
    unittest.main()