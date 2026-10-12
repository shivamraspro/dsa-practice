# from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {']': '[', '}': '{', ')': '(',}
        st = deque()

        for ch in s:
            if ch in mp:
                if len(st) > 0 and st[-1] == mp[ch]:
                    st.pop()
                else:
                    st.append(ch)
            else:
                st.append(ch)
        
        return len(st) == 0