class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        set_ = set(s)
        for i in range(len(s)):
            if s[i].lower() in set_ and s[i].upper() in set_:
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
        return s
        
        
        