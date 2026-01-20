class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[len(skill)-1]
        i = 0
        j = len(skill)-1
        res = 0
        while i < j:
            if skill[i] + skill[j] == target:
                res += skill[i] * skill[j]

            else:
                return -1
            i += 1
            j -= 1
          
    
        return res
                




                                                                                                                                                                                                               
        