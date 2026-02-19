class Solution:

    def simplifyPath(self, path: str) -> str:
            stack = []
            paths = path.split("/")
            for pstr in paths:
                if pstr == "" or pstr ==".":
                    continue
                elif pstr == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(pstr)
                    
            return '/'+'/'.join(stack)
    
 
               



            

        