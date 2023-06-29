Link : https://leetcode.com/problems/unique-number-of-occurrences/

Code :

def uniqueOccurrences(self, arr: List[int]) -> bool:
    # dic = {}
    # l = []
    # for i in arr:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1
    # for i in dic.values():
    #     l.append(i)
    # x = []
    # for i in l:
    #     if l.count(i) > 1:
    #         x.append(i)    
    # if len(x) == 0:
    #     return True
    # return False

    # dic = {}
    # for i in arr:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1
    # return len(dic) == len(set(dic.values()))

    dic = collections.Counter(arr)
    l = [i for i in dic.values()]        
    nums = [i for i in l if l.count(i) > 1]
    return len(nums) == 0
