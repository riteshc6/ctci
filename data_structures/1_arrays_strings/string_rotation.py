import unittest

def get_start_index_of_substring(s1, s2):
    start_index = None
    idx1 = 0
    for idx2 in range(len(s2)):
        if start_index:
            if s1[idx1] == s2[idx2]:
                idx1 += 1
            else:
                start_index = None
                idx1 = 0
        elif s2[idx2] == s1[0]:
            start_index = idx2
            idx1 = 1
    return start_index

def string_rotation(s1, s2):
    """
        checks if s2 is a rotation of s1
    """
    len_s1 = len(s1) 
    len_s2 = len(s2)
    if not len_s1 and not len_s2: return False
    
    if len_s1 != len_s1 : return False

    start_index = get_start_index_of_substring(s1, s2)

    if start_index:
        s2_without_rotation = s2[start_index:] + s2[:start_index]

        if s2_without_rotation == s1:
            return True
        else:
            return False
    else:
        return False


class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('let it be', 'it be tel', False),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):

        for s1, s2, expected in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
