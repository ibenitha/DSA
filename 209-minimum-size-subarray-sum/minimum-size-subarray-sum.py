class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_length = float('inf')
        for r in range (len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                curr_sum -= nums[l]
                min_length = min(r - l + 1, min_length)
                l += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length
                    
                    
                








        