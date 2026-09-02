class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif not stack:
                return False

            elif stack[len(stack) - 1] == '(' and s[i] != ')':
                return False
            elif stack[len(stack) - 1] == '{' and s[i] != '}':
                return False
            elif stack[len(stack) - 1] == '[' and s[i] != ']':
                return False
            else: stack.pop(len(stack) - 1)
        
        if not stack: return True
        return False
