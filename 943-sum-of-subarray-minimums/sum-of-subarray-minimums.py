
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n
        res = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack) == 0:
                left[i] = i+1
            else:
                left[i] = i - stack[-1]
            stack.append(i)
            res += arr[i] * left[i] * right[i]

        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)
            res += arr[i] * left[i] * right[i]
        return res % (10**9 + 7)