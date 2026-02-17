class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        length, l, sign = 1, 0, -1
        for r in range(1, n):
            if arr[r-1] > arr[r] and sign != 0:
                sign = 0
            elif arr[r] > arr[r-1] and sign != 1:
                sign = 1
            elif arr[r] == arr[r-1]:
                l = r
            else:
                l = r - 1
                sign = 0 if arr[r-1] > arr[r] else 1
            length = max(length, r - l + 1)

        return length
