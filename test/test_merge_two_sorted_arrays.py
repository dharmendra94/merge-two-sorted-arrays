import unittest

from code.merge_two_sorted_arrays import mergeSortedArrays, parseCommandLineArgs

class TestMergeTwoSortedArrays(unittest.TestCase): 
        
    def test_merge_two_sorted_arrays(self):
        """
        Test that it can merge two sorted arrays
        """
        self.assertEqual(mergeSortedArrays([1,2], [3,4,5]), [1, 2, 3, 4, 5], "Should return [1, 2, 3, 4, 5]")

    def testParseCommandLineArgsWithOutSpaces(self):
        """
        Test that it can parse the arguments without spaces between the array elements to list and return a tuple with two lists
        """
        self.assertEqual(parseCommandLineArgs("[1,2] [3,4]"), ([1, 2], [3,4]), "Should return a tuple ([1, 2], [3, 4])")

    def testParseCommandLineArgsWithSpaces(self):
        """
        Test that it can parse the arguments with spaces between the array elements to list and return a tuple with two lists
        """
        self.assertEqual(parseCommandLineArgs("[1, 2] [1, 2]"), ([1, 2], [1, 2]), "Should return a tuple ([1, 2], [1, 2])")

    def testParseCommandLineArgsWithAnEmptyArray(self):
        """
        Test that it can parse the arguments with one empty array to list and return a tuple with two lists
        """
        self.assertEqual(parseCommandLineArgs("[1,2] []"), ([1, 2], []), "Should return a tuple ([1, 2], [])")


if __name__ == "__main__":
    unittest.main()