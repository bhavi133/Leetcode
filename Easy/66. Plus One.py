Link : https://leetcode.com/problems/plus-one/

Code :

def plusOne(self, digits: List[int]) -> List[int]:
    # s = ""
    # for i in digits:
    #     s += str(i)
    # x = int(s) + 1  
    # y = str(x)
    # l = []
    # for i in list(y):
    #     l.append(int(i))
    # return l

    s = ""
    for i in digits:
        s += str(i)
    l = [int(i) for i in str(int(s) + 1)]
    return l
