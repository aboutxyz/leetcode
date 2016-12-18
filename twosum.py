class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            else:
                d[num] = i

nums = [1,2,2, 7, 11, 15, 3, 6, 78]
target = 21

a= Solution()
print a.twoSum(nums, target)
