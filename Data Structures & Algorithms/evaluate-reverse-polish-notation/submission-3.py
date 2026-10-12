class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ('+', '-', '*', '/')
        st = []
        res = 0
        
        for tk in tokens:
            if tk in ops:
                second = int(st.pop())
                first = int(st.pop())
                if tk == '+':
                    res = first + second
                elif tk == '-':
                    res = first - second
                elif tk == '*':
                    res = first * second    
                elif tk == '/':
                    res = first / second
                
                st.append(res)
            else:
                st.append(tk)
        
        return res if not st else int(st.pop())