class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        res = 0
        remain_cnt = defaultdict(int)
        remain_cnt[0] = 1

        for num in nums:
            prefix_sum += num

            remain = prefix_sum % k

            res += remain_cnt[remain]

            remain_cnt[remain] += 1

        return res

            

            



                
                
        