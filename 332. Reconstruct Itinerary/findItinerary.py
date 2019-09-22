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
        def dfs(city):
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
        return dfs("JFK")


'''
Follow up question:
What if the initial origin is not given? How would you find out the initial origin?

Conditions for a directed graph:

A directed graph has an eulerian circuit if and only if it is connected and each vertex has the same in-degree as out-degree. In this case we can choose any node as the start node.
A directed graph has an eulerian trail if and only if it is connected and each vertex except 2 have the same in-degree as out-degree, and one of those 2 vertices has out-degree with one greater than in-degree (this is the start node), and the other vertex has in-degree with one greater than out-degree (this is the end node).

What is the time complexity?

O(Vlog(V) + E), V for nubmer of cities, E for number of tickets

What is the space complexity?

'''
