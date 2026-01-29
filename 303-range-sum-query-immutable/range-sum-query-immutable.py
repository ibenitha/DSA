class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sumnum = 0

        for i in range(left, right+1):
            sumnum += self.nums[i]
    
        return sumnum


