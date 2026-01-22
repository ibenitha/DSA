class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curr_longest = 0
        
        substr = []
        for _ in range(len(s)):
            while l <= r and l < len(s) and r < len(s):
                if s[r] not in substr:
                    substr.append(s[r])
                    curr_longest = max(r - l +1, curr_longest)
                    r += 1
                    print(curr_longest)
                else:
                    substr.remove(s[l])
                    l += 1
                    
        return curr_longest
                





        