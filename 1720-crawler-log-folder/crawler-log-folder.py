class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for d in logs:
            if d =="./":
                continue
            elif d != "../":
                stack.append(d)
            
            else:
                if stack:
                    stack.pop()
           
        return len(stack)

        