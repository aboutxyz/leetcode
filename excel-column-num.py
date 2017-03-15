class Solution(object):
    def titleToNumber(self, s):
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))

a = Solution()
print a.titleToNumber('BA')


def Numbertotitle(n):
    r = ''
    while(n>0):
        n = n-1
        r = chr(n%26+65) + r
        n = n/26
    return r    
print Numbertotitle(27)