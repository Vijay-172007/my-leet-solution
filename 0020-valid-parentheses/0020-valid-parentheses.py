class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={')':'(','}':'{',']':'['}
        for i in s:
            if i in d:
                if not st or st.pop()!=d[i]:
                    return False
            else:
                st.append(i)
        return not st
