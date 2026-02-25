class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1]* len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                top = stack.pop()
                ans[top] = nums2[i]
            stack.append(i)
        dictr={}
        i=0
        for num in nums2:
            dictr[num]=ans[i]
            i+=1
        return [dictr[num] for num in nums1]

        

        

       


        


        

        
    

    

        

        
        