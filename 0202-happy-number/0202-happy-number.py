class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            t=0
            while n>0:
                digit=n%10
                t+=digit*digit
                n//=10
            n=t        
        return n==1