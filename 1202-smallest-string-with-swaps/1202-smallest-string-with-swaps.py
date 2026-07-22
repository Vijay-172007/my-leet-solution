class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = list(range(len(s)))

        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        for a, b in pairs:
            p[find(a)] = find(b)

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[find(i)].append(c)

        for v in d.values():
            v.sort(reverse=True)

        return "".join(d[find(i)].pop() for i in range(len(s)))