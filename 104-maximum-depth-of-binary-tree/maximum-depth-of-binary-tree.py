# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        stack = [(root,1)]

        max_d = 0

        while stack:
            root,dep = stack.pop()
            if root:
                max_d = max(max_d,dep)
                stack.append((root.left,dep+1))
                stack.append((root.right, dep+1))

           
        return max_d

        
        