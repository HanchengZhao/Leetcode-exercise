from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # make a map to save des: stop
        to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_route[j].add(i)
        # 0 is number of buses taken
        queue = deque([[S, 0]])
        visited = set()
        while queue:
            stop, bus = queue.popleft()
            if stop == T:
                return bus
            for i in to_route[stop]:
                for r in routes[i]:
                    if r not in visited:
                        queue.append([r, bus+1])
                        visited.add(r)
                routes[i] = []  # seen route
        return -1

# https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution
