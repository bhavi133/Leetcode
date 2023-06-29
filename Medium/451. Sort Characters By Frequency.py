Link : https://leetcode.com/problems/sort-characters-by-frequency/

Code :

import collections

def frequencySort(self, s: str) -> str:
    # dic = {}
    # l = ""
    # for i in s:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1
    # for i in sorted(dic.items(), reverse=True, key=lambda x : x[1]):
    #     l = l + (i[0] * i[1])
    # return l

    dic = collections.Counter(s)
    l = ""
    for i in sorted(dic.items(), reverse=True, key=lambda x : x[1]):
        l = l + (i[0] * i[1])
    return l
