class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+':
                b = int(st.pop())
                a = int(st.pop())
                st.append(a + b)
            elif t == '-': 
                b = int(st.pop())
                a = int(st.pop())
                st.append(a - b)
            elif t == '*': 
                b = int(st.pop())
                a = int(st.pop())
                st.append(a * b)
            elif t == '/':
                b = int(st.pop())
                a = int(st.pop())
                st.append(a / b)
            else:
                st.append(t)
        return int(st[0])
