class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        R =0
        max_sum = 0
        while R < k:
            max_sum += nums[R]
            R += 1
            
        if k >= len(nums):
            return max_sum / k
        
        left =0
        average = 0
        curr_sum = max_sum
        for right in range(k, len(nums)):
            curr_sum = curr_sum - nums[left] + nums[right]
            if max_sum < curr_sum:
                max_sum = curr_sum
            average = max_sum/k 
            left += 1
        return average

    



