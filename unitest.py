import mymath
import unittest
 
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
 
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1,4)
        self.assertEqual(result, 3)
 
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)
 
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdek')
 
unittest.main()


