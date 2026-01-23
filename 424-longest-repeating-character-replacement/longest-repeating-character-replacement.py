class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, most_freq_char, res, freq = 0,0,0,0, defaultdict(int)
        while r < len(s):
            freq [s[r]] += 1
        
            most_freq_char = max(most_freq_char, freq[s[r]])

            while (r-l +1) - most_freq_char > k:
                
                freq[s[l]] -= 1
                l += 1 
            res = max(res,r -l +1)
            r += 1
        return res
        
    
            



        

        