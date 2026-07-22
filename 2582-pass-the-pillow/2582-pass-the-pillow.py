class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cyc=n-1
        pos=time%(2*cyc)
        if pos<=cyc:
            return pos+1
        return 2*cyc-pos+1
        