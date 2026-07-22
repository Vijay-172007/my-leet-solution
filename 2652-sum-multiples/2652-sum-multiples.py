class Solution:
    def sumOfMultiples(self, n: int) -> int:
         return sum(i for i in range(n + 1) if i % 3 * i % 5 * i % 7 == 0)
        