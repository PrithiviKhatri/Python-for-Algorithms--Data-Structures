# Given an integer array, output all the unique pairs that sum up to a specific value k.
#
# So the input:
#
# pair_sum([1,3,2,2],4)
#
# would return 2 pairs:
#
#  (1,3)
#  (2,2)
import unittest


# following algorithm is in O(n^2)
# def pair_sum(arr, k):
#     output = set()
#     for i, n in enumerate(arr):
#         other_value = k - n
#         if other_value in arr[i + 1:]:
#             output.add((min(n, other_value), max(n, other_value)))
#
#     return len(output)

# following alogirithm is in O(n)
def pair_sum(arry, k):
    if len(arry) < 2:
        return
    output = set()
    seen = set()
    for num in arry:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


class TestPair(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(pair_sum([1, 2, 3, 1], 3), 1)
        self.assertEqual(pair_sum([1, 3, 2, 2], 4), 2)
        self.assertEqual(pair_sum([1, 1, 2], 4), 0)

        print 'ALL TEST CASES PASSED'


if __name__ == "__main__":
    unittest.main()
