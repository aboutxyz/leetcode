#coding:utf-8
findNums = [4,1,2]
nums = [1,3,4,2]
print [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

d = {}
st = []
ans = []

for x in nums:
    while len(st) and st[-1] < x:
        d[st.pop()] = x
    st.append(x)

for x in findNums:
    ans.append(d.get(x, -1))
    
print ans

'''
st 1
d[1] = 3
st 3
d[3] = 4
st 4
st 4,2
'''


