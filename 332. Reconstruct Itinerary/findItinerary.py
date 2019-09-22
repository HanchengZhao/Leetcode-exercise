from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.trips = defaultdict(list)
        self.path = ["JFK"]
        for t in sorted(tickets):
            self.trips[t[0]].append(t[1])

        # backtrack to see if the city would be the good choice
        # otherwise append it back to try other cities
        # the first path it returns will be the lowerst in lexical order
        def dfs(city="JFK"):
            if len(self.path) == len(tickets) + 1:
                return self.path
            nxtTrips = sorted(self.trips[city])
            for nxt in nxtTrips:
                self.trips[city].remove(nxt)
                self.path.append(nxt)
                worked = dfs(nxt)
                if worked:
                    return worked
                self.trips[city].append(nxt)
                self.path.pop()
        return dfs()
