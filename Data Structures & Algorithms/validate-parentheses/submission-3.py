class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if st and s[i] == ')' and st[-1] == '(':
                st.pop()
            elif st and s[i] == '}' and st[-1] == '{':
                st.pop()
            elif st and s[i] == ']' and st[-1] == '[':
                st.pop()
            else:
                st.append(s[i])

        return not st