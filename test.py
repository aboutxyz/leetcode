# coding:utf-8

ss = "abcabdc"
d = {}
long = []
for i in range(len(ss)):
    if ss[i] in d:
        long.append(i-d[ss[i]])
        d[ss[i]] = i
    else:
        d[ss[i]] = i
print max(long)