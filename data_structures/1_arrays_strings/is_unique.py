import unittest

def is_unique(string):

    char_counter = [0] * 128

    for c in string:
        index = ord(c)
        if char_counter[index] > 0:
            return  False
        char_counter[index] += 1
    return True

 



class Test(unittest.TestCase):
    dataT = ["ldj8*{}", "[]()skjfdvio"]
    dataF = ["aldfkdflksajfk", "a;df;dkfj"]

    def test_unique(self):
        for data in self.dataT:
            result = is_unique(data)
            self.assertTrue(result)
        
        for data in self.dataF:
            result = is_unique(data)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
