import unittest

def check_permutation(string1, string2):
    
    if len(string2):
        # Creating an array to keep track of all characters in string1
        char_counter = [0] * 128
        for c in string1:
            index = ord(c)
            char_counter[index] += 1
        
        for c in string2:
            index = ord(c)
            char_counter[index] -= 1
            if char_counter[index] < 0:
                return False
        return True
    else:
        return False


class Test(unittest.TestCase):

    # dataT = [("shsdhj*&#2,cvals", "lv,&*#2s"), ("shiterskljdka;lfd", "lkd;ashi")]
    # dataF = [("dsljffjfjtirtugasjfklsjdkjjkjfkjsfknvnjan;zf", 'dfjkgjlsdgjfdlgjlfg;jldgjdfjghrug='), ("&**()*(*Q##$#)#", "skldjfhfjkhsdgjhfdkjhfjksdhjkafhd")]
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
        ('abcd', 'abbcd')        # Makes sure that the algo is written for perm with repitition. Note: Try for PR for this test case
    )

    def test_check_permutation(self):

        for string1, string2 in self.dataT:
            actual = check_permutation(string1, string2)
            self.assertTrue(actual)
        
        for string1, string2 in self.dataF:
            actual = check_permutation(string1, string2)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()