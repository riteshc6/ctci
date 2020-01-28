import unittest

def URLify(string, length):

    string = string.rstrip()    
    string = string.replace(" ", "%20")
    return string



class Test(unittest.TestCase):

    def test_urlify(self):
        data = [
            ('much ado about nothing      ', 22,
            'much%20ado%20about%20nothing'),
            ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

        for url, length, expected_url in data:
            URLified = URLify(url, length)
            self.assertEqual(URLified, expected_url)


if __name__ == "__main__":
    unittest.main()
