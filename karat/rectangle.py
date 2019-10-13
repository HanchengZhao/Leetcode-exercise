'''
1. ⼀一个矩阵，只有0和1，找到⾥里里⾯面全为1的矩形的坐标。输⼊入⼀一定有效，保 证有⼀一个满⾜足要求的矩形。⽤用左上和右下坐标表示
⽐比如:
0 0 0 0 0. ⽜牛⼈人云集,⼀一亩三分地
0 1 1 0 0. more info on 1point3acres 00000
结果就是返回
[1,1], [1,2]
2. follow up 有很多个这样的矩形， 返回所有的矩形的左上右下坐标 3. 不不⼀一定是矩形，找出所有连通的1. . from: 1point3acres
10011
00011
10001
这样的输⼊入，返回⼀一个⼤大数组
[
[0,0],
[[0,3], [0,4], [1,3], [1,4], [2,4]], [2,1]
]

ps.
其‍‍‍‍‌‍‍‌‍‌‍‍‌‍‌‌‌中肯定有且只有一个由0组成的长方体，其他全是1.
找出这个长方体的左上角左边，长方体的长和高。
{
{1,1,1,1,1,1},
{1,0,0,0,1,1},
{1,0,0,0,1,1},
{1,1,1,1,1,1},
{1,1,1,1,1,1}
}
那么返回{1,1,3,2}  坐标为（1,1），长为3，高为2
'''

# 1.
# only one rectangle exists


def find_rectangle(arr):
    m, n = len(arr), len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                start = [i, j]
                end_col = j
                end_row = i
                while end_col < n and arr[i][end_col] == 0:
                    end_col += 1
                while end_row < m and arr[end_row][j] == 0:
                    end_row += 1
                end = [end_row, end_col]
                return [start, end]


print(find_rectangle([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]))

# 2.

input2 = [[1, 1, 1, 1, 1, 1],
          [0, 0, 1, 0, 1, 1],
          [0, 0, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 0],
          [1, 0, 0, 1, 1, 1]]


def visited(arr, start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            arr[i][j] = 1


def find_all_rectangle(arr):
    m, n = len(arr), len(arr[0])
    res = []

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                start = [i, j]
                end_col = j
                end_row = i
                while end_col+1 < n and arr[i][end_col+1] == 0:
                    end_col += 1
                while end_row+1 < m and arr[end_row+1][j] == 0:
                    end_row += 1
                end = [end_row, end_col]
                res.append([start, end])
                visited(arr, start, end)
    return res


# print(find_all_rectangle(input2))


# 3.
def find_islands(arr):
    print(arr)
    if not arr:
        return []
    m, n = len(arr), len(arr[0])
    res = []

    def dfs(arr, i, j, islands):
        if i < 0 or i >= m or j < 0 or j >= n or arr[i][j] != 0:
            return
        row = [0, -1, 1, 0]
        col = [-1, 0, 0, 1]

        islands.append([i, j])
        arr[i][j] = 1
        for k in range(4):
            new_row = row[k] + i
            new_col = col[k] + j
            dfs(arr, new_row, new_col, islands)
    for i in range(m):
        for j in range(n):
            islands = []
            if arr[i][j] == 0:
                dfs(arr, i, j, islands)
                res.append(islands)
    return res


print(find_islands(input2))
