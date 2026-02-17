class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        need = Counter(t)
        window = {}
        have, needCount = 0, len(need)
        left, minLen, start = 0, float("inf"), 0

        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == needCount:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left
                l = s[left]
                window[l] -= 1
                if l in need and window[l] < need[l]:
                    have -= 1
                left += 1
        
        return "" if minLen == float("inf") else s[start:start+minLen]