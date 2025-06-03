class Solution(object):
    def reverse(self, x):
        isneg = x < 0
        res = 0 
        num = abs(x)
        while(num != 0):
            digit = num % 10
            num //= 10
            res = res * 10 + digit
        
        if res > (2**31 - 1):
            return 0 
        return -res if isneg else res