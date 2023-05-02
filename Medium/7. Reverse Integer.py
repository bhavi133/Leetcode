Link : https://leetcode.com/problems/reverse-integer/

Code :

def reverse(self, x: int) -> int:
    if x >= 0:
        result = int(str(x)[::-1])
        if result > (pow(2,31)-1):
            return 0
        else:
            return result
    else:
        result = int(str(x)[1:][::-1])
        if result > (pow(2,31)):
            return 0
        else:
            return int("-" + str(result))
