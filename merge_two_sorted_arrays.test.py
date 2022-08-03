import unittest
import merge_two_sorted_arrays

class TestMergeTwoSortedArrays(unittest.TestCase): 
        
    def test_merge_two_sorted_arrays(self):
        """
        Test that it can merge two sorted arrays
        """
        self.assertEqual(merge_two_sorted_arrays.mergeSortedArrays([1,2], [3,4,5]), [1, 2, 3, 4, 5], "Should return [1, 2, 3, 4, 5]")

    def testParseCommandLineArgs(self):
        """
        Test that it can parse the arguments to list and return a tuple with two lists
        """
        self.assertEqual(merge_two_sorted_arrays.parseCommandLineArgs("[1,2]", "[]"), ([1, 2], []), "Should return a tuple ([1,2], [])")

if __name__ == "__main__":
    unittest.main()