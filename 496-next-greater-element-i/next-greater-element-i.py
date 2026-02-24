class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = [3,4,-1,-1]
        stack = []
        ans = [-1]* len(nums2)
        
    

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                top = stack.pop()
                ans[top] = nums2[i]

            stack.append(i)

        res = []

        for num in nums1:
            for j in range(len(nums2)):
                if nums2[j] == num:
                    res.append(ans[j])
                    break
        return res

       


        


        

        
    

    

        

        
        