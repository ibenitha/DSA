class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        for l, r, d in shifts:
            if d:
                prefix[l] += 1
                prefix[r+1] -= 1
            else:
                prefix[l] -= 1
                prefix[r+1] += 1
        accumulator = 0
        for i in range(len(prefix)):
            accumulator += prefix[i]
            prefix[i] = accumulator
        res = ""
        for idx, char in enumerate(s):
            temp = (ord(char) - ord('a') + prefix[idx])% 26
            res += chr(temp + ord('a'))
        return res

        
        