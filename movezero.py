#coding：utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = operator.not_)
        
        # a.sort(key=lambda x: not x or None)
        
        
        # def moveZeroes(self, nums):
            # zero = 0  # records the position of "0"
            # for i in xrange(len(nums)):
                # if nums[i] != 0:
                    # nums[i], nums[zero] = nums[zero], nums[i]
                    # zero += 1


