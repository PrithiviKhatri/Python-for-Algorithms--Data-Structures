"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""
import unittest
import collections


# not optimal when array is too large or array memebers are too large
# def finder(arr1, arr2):
#     sum_arr1 = sum(arr1)
#     sum_arr2 = sum(arr2)
#     return abs(sum_arr2 - sum_arr1)


def finder(arr1, arr2):
    counter = collections.defaultdict(int)

    for num in arr2:
        counter[num] += 1
    for num in arr1:
        if counter[num] == 0:
            return num
        else:
            counter[num] -= 1




class TestMissingElement(unittest.TestCase):
    def test(self):
        self.assertEqual(finder([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print 'ALL TEST CASES PASSED'


if __name__ == "__main__":
    unittest.main()
