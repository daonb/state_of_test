import unittest

# Some random functional code (just for demonstration)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class BadTestSuite(unittest.TestCase):

    CONSTANTS = [3, 7, 10]

    def helper_function(self, x, y):
        return x * y + self.CONSTANTS[1]

    def test_complicated_addition(self):
        for i in range(1, 5):
            for j in self.CONSTANTS:
                self.assertEqual(add(i, j), self.helper_function(i, j))

    def test_unrelated_maths(self):
        magic_numbers = [i for i in range(10) if i % 2 == 0]
        for magic in magic_numbers:
            self.assertEqual(multiply(magic, 3), add(magic, self.CONSTANTS[2]))

if __name__ == "__main__":
    unittest.main()

