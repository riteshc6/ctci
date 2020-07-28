import unittest

def URLify(string: str, true_length: int):

    space_count = 0
    for i in range(true_length):
        if string[i] == " ":
            space_count += 1
    
    index = true_length + (2 * space_count) - 1
    for i in range(true_length - 1, -1, -1):
        if string[i] == " ":
            string[index] = "0"
            string[index - 1] = "2"
            string[index - 2] = "%"
            index -= 3
        else:
            string[index] = string[i]
            index -= 1
    
    return string



class Test(unittest.TestCase):

    def test_urlify(self):
        data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

        for url, length, expected_url in data:
            URLified = URLify(url, length)
            self.assertEqual(URLified, expected_url)


if __name__ == "__main__":
    unittest.main()
