# https://leetcode.com/problems/jewels-and-stones/

# My solution
from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([value for key, value in Counter(S).items() if key in J])
      
# Solution 1: Remove stones in S that are jewels, deduce removed amount. This
# method appears to be fastest, I don't understand why
class Solution1:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        b = S
        for a in J:
            b = b.replace(a, '')
        return len(S) - len(b)
      
# Solution 2: Use the boolean/integer equivalence
class Solution2:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([s in J for s in S])
        