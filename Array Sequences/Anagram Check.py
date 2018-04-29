"""Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

"""
import unittest


# def anagram(s1, s2):
#     is_anagram = False
#     s1 = [x.lower() for x in s1.replace(" ", "") if x]
#     s2 = [x.lower() for x in s2.replace(" ", "") if x]
#     if sorted(s1) == sorted(s2):
#         is_anagram = True
#     return is_anagram

# more efficient way , avoiding sorting and again comparing the list
def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    counter = {}
    for x in s1:
        if x in counter:
            counter[x] +=1
        else:
            counter[x] =1

    for x in s2:
        if x in counter:
            counter[x] -= 1
        else:
            return  False

    for x in counter:
        if counter[x] != 0:
            return False
    return True


class AnagramTest(unittest.TestCase):
    def test(self):
        self.assertEqual(anagram('go go go', 'gggooo'), True)
        self.assertEqual(anagram('abc', 'cba'), True)
        self.assertEqual(anagram('hi man', 'hi     man'), True)
        self.assertEqual(anagram('aabbcc', 'aabbc'), False)
        self.assertEqual(anagram('123', '1 2'), False)
        print "ALL TEST CASES PASSED"


if __name__ == "__main__":
    unittest.main()
