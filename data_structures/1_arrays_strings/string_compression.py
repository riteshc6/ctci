import unittest

def compress_string(string):
    if not string: return string
    repetition_count = 0
    repeating_char = string[0]
    compressed_array = []

    for char in string:
        if repeating_char == char:
            repetition_count += 1
        else:
            compressed_array.append(repeating_char + str(repetition_count))
            repeating_char = char
            repetition_count = 1
    compressed_array.append(repeating_char + str(repetition_count))
    compressed_string = "".join(compressed_array)
    return compressed_string if len(string)>len(compressed_string) else string



class Test(unittest.TestCase):

    data = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('aabb', 'aabb'),
            ('',''),
            ('bcdef', 'bcdef')
        ]

    def test_compress_string(self):
        
        for string, expected in self.data:

            actual = compress_string(string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()