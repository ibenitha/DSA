class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        res = 1
        for j in range(k + 1):
            max1 = 1
            num_map = {nums[0]: 0}

            for i in range(1, n):
                dp[i][j] = 1
                if i > 0 and j > 0:
                    max1 = max(max1, dp[i - 1][j - 1] + 1)
                dp[i][j] = max(dp[i][j], max1)

                if nums[i] in num_map:
                    dp[i][j] = max(dp[i][j], dp[num_map[nums[i]]][j] + 1)

                num_map[nums[i]] = i
                res = max(res, dp[i][j])

        return res

        