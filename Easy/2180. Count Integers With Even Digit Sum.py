Link : https://leetcode.com/problems/count-integers-with-even-digit-sum/

Code :

def countEven(self, num: int) -> int:
    # l = []
    # count = 0
    # for i in range(1, num+1):
    #     l.append(sum(map(int, str(i))))
    # for i in l:
    #     if i % 2 == 0:
    #         count += 1
    # return count

    l = [sum(map(int, str(i))) for i in range(1, num+1)]
    return len([i for i in l if i % 2 == 0])
