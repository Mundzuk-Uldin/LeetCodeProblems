class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in parenthesis.keys():
                last_char = ''
                if len(stack) > 0:
                    last_char = stack.pop()
                if last_char != parenthesis[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True
