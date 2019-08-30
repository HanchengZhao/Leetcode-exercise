import heapq


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        h = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                heapq.heappush(h, (dist, i, j))
        res = [-1 for i in range(len(workers))]
        visited = set()
        while h:
            nxt = heapq.heappop(h)
            w, b = nxt[1], nxt[2]
            if res[w] == -1 and b not in visited:
                res[w] = b
                visited.add(b)
        return res
