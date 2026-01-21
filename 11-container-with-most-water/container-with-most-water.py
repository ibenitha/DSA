class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        while i <=j:
            if height[i] < height[j]:
                height[i] *= (j-i)
                i += 1
            else:
                height[j] *= (j-i)
                j -= 1

        return max(height)

            
        