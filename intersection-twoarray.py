#coding:utf-8

"""
两个列表重合部分，相同元素忽略
"""
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print list(set(nums1)&set(nums2))


"""
两个列表重合部分，相同元素不忽略
"""
from collections import Counter
def intersect(nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    return list((a & b).elements())
    
    
print intersect(['a','cf', 'gg'], ['g','gg'])