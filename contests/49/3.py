class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest:
            return -1
        dic = {}
        m = len(forest)
        n = len(forest[0])
        trees = []
        for i in xrange(m):
            for j in xrange(n):
                if forest[i][j] != 0:
                    trees.append(forest[i][j])
                    dic[forest[i][j]] = (i,j)
        last = (0,0)
        total = 0
        for i in sorted(trees):
            nxt = dic[i]
            if nxt != last:
                total += self.distance(nxt,last,forest)
                last = nxt
        return total if total != 0 else -1

    def distance(self, t1, t2, forest):
        m = len(forest)
        n = len(forest[0])
        x, y = t1
        xs = [-1,1,0,0]
        ys = [0,0,-1,1]
        queue = [(x,y)]
        length = 0
        visited = set()
        visited.add((x,y))
        while queue:
            x1, y1 = queue.pop(0)
            if (x1, y1) == t2:
                return length
            for i in xrange(4):
                if x1+i > 0 and x1+i < m and y1+i > 0 and y1+i < n:
                    if forest[x1+i][y1+i] != 0 and (x1+i, y1+i) not in visited:
                        queue.append((x1+1, y1+i))
                        visited.add((x1+1, y1+i))
            length += 1
        return -1

s = Solution()
print s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]])