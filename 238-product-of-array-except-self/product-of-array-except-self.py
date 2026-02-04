class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        prefix [0]= nums[0]
        suffix = [1]* len(nums)
        suffix [len(nums)-1] = nums[len(nums)-1]
        ans = []


        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(len(nums)-2,-1,-1):
            suffix [i] = suffix[i+1] * nums[i]
        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix[i+1])
            elif i == len(nums)-1:
                ans.append(prefix[i-1])
            else:
                ans.append( suffix[i+1]* prefix[i-1])
        return ans

        





     

      
        
    


             


        