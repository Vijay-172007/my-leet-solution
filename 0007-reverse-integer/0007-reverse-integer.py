class Solution:
    def reverse(self, x: int) -> int:
        sign=False
        if x<0:
            sign=True
            x*=-1
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev>2**31-1:
            return 0
        return rev*-1 if sign else rev
