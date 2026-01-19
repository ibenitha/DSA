class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            for w in strs:
                if i >= len(w) or w[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix
