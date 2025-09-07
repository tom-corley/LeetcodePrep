from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        r_voters = 0
        d_voters = 0
        r_bans = 0
        d_bans = 0
        for member in senate:
            if member == 'R':
                r_voters += 1
            else:
                d_voters += 1
            q.append(member)
        
        while r_voters and d_voters:
            voter = q.popleft()
            if voter == 'R':
                if d_bans > 0:
                    d_bans -= 1
                    r_voters -= 1
                else:
                    r_bans += 1
                    q.append(voter)
            if voter == 'D':
                if r_bans > 0:
                    r_bans -= 1
                    d_voters -= 1
                else:
                    d_bans += 1
                    q.append(voter)
        if d_voters == 0:
            return "Radiant"
        else:
            return "Dire"
        