# https://leetcode.com/problems/two-sum/

# Build incrementally a hash table items of the form {number : index_of number},
# return when pair is found
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

# Worse solution without a hash 
class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_nums = sorted(enumerate(nums), key=lambda t : t[1]) 
        first, last = 0, len(nums)-1
        while index_nums[first][1] + index_nums[last][1] != target:
            if index_nums[first][1] + index_nums[last][1] < target:
                first += 1
            else:
                last -= 1
        return [index_nums[first][0], index_nums[last][0]]