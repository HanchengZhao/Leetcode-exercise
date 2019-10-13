class Solution:
    def queensAttacktheKing(self, queens, king):
        n = 8
        res = []
        x, y = king
        # left
        for i in range(x, -1, -1):
            if [i, y] in queens:
                res.append([i, y])
                break
        # right
        for i in range(x, n):
            if [i, y] in queens:
                res.append([i, y])
                break
        # up
        for i in range(y, -1, -1):
            if [x, i] in queens:
                res.append([x, i])
                break
        # down
        for i in range(y, n):
            if [x, i] in queens:
                res.append([x, i])
                break
        # top left
        for i in range(1, min(x, y)+1):
            if [x - i, y - i] in queens:
                res.append([x - i, y - i])
                break
        # top right
        for i in range(1, min(x, n-1-y)+1):
            if [x - i, y + i] in queens:
                res.append([x - i, y + i])
                break
         # bottom left
        for i in range(1, min(n-1-x, y)+1):
            if [x + i, y - i] in queens:
                res.append([x + i, y - i])
                break
        # bottom right
        for i in range(1, min(n-1-x, n-1-y)+1):
            if [x + i, y + i] in queens:
                res.append([x + i, y + i])
                break
        return res


s = Solution()
print(s.queensAttacktheKing(
    [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], [3, 3]))
