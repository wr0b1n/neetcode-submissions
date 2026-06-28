class Solution:
    def isValid(self, s: str) -> bool:

        dic = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }
        stack = []

        for c in s:
            # opening brackets are pushed to the stack
            if c in dic.values():
                stack.append(c)             

            # closing brackets must match the top element in the stack
            elif c in dic.keys():
                if len(stack) <= 0:
                    return False

                elem = stack.pop()
                if elem != dic[c]:
                    return False
        
        return len(stack) == 0
