class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        target = Counter(s1)
        for r in range(len(s1),len(s2)+1):
            window = Counter (s2[l:r])
            if target == window:
                return True
            l += 1
        return False
            
    

        

        
        