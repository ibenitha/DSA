class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        target = Counter(p)
        res = []
        for r in range (len(p),len(s)+1):
            window = Counter(s[l:r])
            if target == window:
                res.append(l)
            l += 1
        return res





            
     