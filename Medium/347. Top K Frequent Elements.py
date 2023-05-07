Link : https://leetcode.com/problems/top-k-frequent-elements/

Code :

import collections

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = {}
        # l = []
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # for i in sorted(dic.items(), reverse=True, key=lambda x : x[1]):
        #     l.append(i[0])
        # return l[:k]

        dic = collections.Counter(nums)
        l = [i[0] for i in sorted(dic.items(), reverse=True, key=lambda x : x[1])]
        return l[:k]
