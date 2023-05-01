Link : https://leetcode.com/problems/palindrome-number/

Code :

def isPalindrome(self, x: int) -> bool:
    # if str(x) == str(x)[::-1]:
    #     return True
    # return False

    # return str(x) == str(x)[::-1]

    num = x
    rev = 0
    while (x > 0):
        dig = x % 10
        rev = rev * 10 + dig
        x = x // 10
    return (num == rev)
