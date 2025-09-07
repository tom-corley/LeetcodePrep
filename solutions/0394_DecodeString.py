class Solution:
    def decodeString(self, s: str) -> str:
        # Stack of left brackets
        stack = []
        i = 0
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr = []
                while stack[-1] != "[":
                    curr = [stack.pop()] + curr
                stack.pop()
                str_num = ""
                while stack and stack[-1].isdigit():
                    str_num = str(stack.pop()) + str_num
                stack = stack + int(str_num) * curr
        return "".join(stack)
        