Link : https://leetcode.com/problems/divide-two-integers/

Code :

def divide(self, dividend: int, divisor: int) -> int:
    return int(dividend / divisor) if int(dividend // divisor) >= -2**31 and int(dividend // divisor) <= 2**31-1 else 2**31-1
