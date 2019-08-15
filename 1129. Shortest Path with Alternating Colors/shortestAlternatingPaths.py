from typing import List

# the basic idea is to use bfs to traverse all the routes and save the shortest paths
# the key point is how to change color for searching


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # red, blue
        reds = {}
        blues = {}
        for i in red_edges:
            if i[0] not in reds:
                reds[i[0]] = [i[1]]
            else:
                reds[i[0]].append(i[1])
        for i in blue_edges:
            if i[0] not in blues:
                blues[i[0]] = [i[1]]
            else:
                blues[i[0]].append(i[1])
        res = [float("inf")] * n
        g = [reds, blues]

        def bfs(color):
            # save (node, color, step)
            queue = [(0, color, 0)]
            visited = set()
            visited.add((0, color))
            while queue:
                node, c, step = queue.pop(0)
                res[node] = min(res[node], step)
                # this is a trick to change color
                nxtColor = 1 - c
                if node in g[nxtColor]:
                    for n in g[nxtColor][node]:
                        if (n, nxtColor) not in visited:
                            # search in nxt color
                            queue.append((n, nxtColor, step+1))
                            visited.add((n, nxtColor))
        # start from red and blue separately
        bfs(0)
        bfs(1)
        return [-1 if i == float("inf") else i for i in res]


if __name__ == "__main__":
    s = Solution()
    print(s.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []))
