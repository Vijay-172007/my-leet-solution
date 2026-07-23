class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for d in digits:
            n = n * 10 + d
        n += 1
        result = []
        while n > 0:
            result.append(n % 10)
            n //= 10
        result.reverse()
        return result