class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumnum = 0
        res = []

        for i in range(len(nums)):
            sumnum += nums[i]
            res.append(sumnum)
        return res
