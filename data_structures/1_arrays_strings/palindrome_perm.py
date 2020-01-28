import unittest

def get_char_frequency(string):

    char_frequency = {}
    for char in string:
        if char.isalnum():
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    return char_frequency


def one_odd_char_present(char_frequency):
    count_odd = 0
    for val in char_frequency.values():
        if val % 2 != 0:
            count_odd += 1
            if count_odd > 1:
                return False
    return True

def check_palindrome_permutation(string):
    string = string.lower()
    char_frequency = get_char_frequency(string)
    return one_odd_char_present(char_frequency)



class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_check_palindrome_permutation(self):
        
        for string, expected in self.data:
            print(string)
            actual = check_palindrome_permutation(string)
            self.assertEqual(actual, expected)

            
if __name__ == "__main__":
    unittest.main()