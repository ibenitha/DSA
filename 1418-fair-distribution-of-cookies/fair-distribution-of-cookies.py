class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def solve(ind,dist):
            if ind==len(cookies):
                maxi=max(dist)
                self.ans=min(self.ans,maxi)
                return

            for i in range(k):
                dist[i]+=cookies[ind]
                if max(dist)<self.ans:
                    solve(ind+1,dist)
                dist[i]-=cookies[ind]
        self.ans=float('inf')
        dist=[0 for i in range(k)]
        cookies.sort(reverse=True)
        solve(0,dist)
        return self.ans
        