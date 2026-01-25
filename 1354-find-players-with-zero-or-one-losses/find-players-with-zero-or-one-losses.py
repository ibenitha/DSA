class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = []
        for w, l in matches:
            losers.append(l)


        lossCount= Counter(losers)
        players = set()

        for w, l in matches:
            players.add(w)
            players.add(l)
        zero_loss = []
        one_loss = []

        for p in players:
            if lossCount[p] == 0:
                zero_loss.append(p)
            elif lossCount[p] == 1:
                one_loss.append(p)
              



        return [sorted(zero_loss), sorted(one_loss)]

        
        