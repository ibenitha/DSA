class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        

        def bothString(string):
            stack = []

            for c in string:
                if c != "#":
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return stack    
        return bothString(s) == bothString(t)

            