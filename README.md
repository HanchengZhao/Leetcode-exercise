## Python tricks

Python 越来越多地成为大家刷题的主流语言，主要原因是它的语法非常简洁明了。因此我们能节省更多的时间，来关注算法和数据结构本身。

而用好 Python 自身独有的一些语法特性，不仅能更节省时间，也能让代码看起来更加优雅。这里我总结了一些我自己刷题过程中用到的一些常用的功能。以下以 python3 为例， python2 略有差异。

## List

Python 的列表 List 基本就是其它语言的 Array.

### Initialization 初始化

List 的初始化一般用 List comprehension，往往能一行解决问题

```python
# 1d array
l = [0 for _ in range(len(array)]

# 2d
l = [[0] for i in range(cols) for j in range(rows)]
```

### Start from the behind

你可以轻松从后往前访问：

```python

lastElement = l[-1]

lastTwo = l[-2:]

for i in range(0, -10, -1)
# 0, -1, -2, -3, -4, -5, -6, -7, -8, -9
```

### copy 复制

#### shallow copy 浅拷贝

```
l2 = l1[:]
# or
l2 = l1.copy()
```

浅复制的问题在于，如果 l1 内部还有 list，那么这种嵌套的索引不能被复制，比如：

```
a = [1, 2, [3, 4]]
b = a[:]
a[2].append(5)
print(b)
# [1, 2, [3, 4, 5]]
```

#### deep copy 深拷贝

所以如果要做深拷贝，要节制自带库 `copy`

```
import copy

copy.deepcopy()
```

### enumerate 枚举

当我们需要枚举一个数组并同时获得值与 index 的时候可以使用：

```
l = ["a", "b", "c"]

for i, v in enumerate(l):
    print(i, v)
# 0 a
# 1 b
# 2 c
```

### zip

`zip` 本意就是拉链，可以想象成将两个数组像拉链一样挨个聚合：

```
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
```

### reduce

`reduce` 可以分别对相邻元素使用同一种计算规则，同时每一步结果作为下一步的参数，很典型的函数式编程用法。

```
# importing functools for reduce()
import functools
# initializing list
lis = [ 1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))

# The sum of the list elements is : 17

```

### map

可以将参数一一映射来计算， 比如

```
date = "2019-8-15"
Y, M, D = map(int, date.split('-'))
# Y = 2019, M = 8, D = 15
```

## deque

list 删除末尾的操作是`O(1)`的，但是删除头操作就是`O(n)`，这时候我们就需要一个双端队列 `deque`。首尾的常规操作为：

- `append`，添加到末尾
- `appendleft`, 添加到开头
- `pop`, 剔除末尾
- `popleft`，移除开头

## sorted

list 自身有自带的 sort(), 但是它不返回新的 list. `sorted` 能返回一个新的 list, 并且支持传入参数`reverse`。

比如我们有一个 tuple 的数组，我们想按照 tuple 的第一个元素进行排序：

```python
l1 = [(1,2), (0,1), (3,10) ]

l2 = sorted(l1, key=lambda x: x[0])

# l2 = [(0, 1), (1, 2), (3, 10)]
```

这里的 key 允许传入一个自定义参数，也可以用自带函数进行比较，比如在一个 string 数组里只想比较小写，可以传入`key=str.lower`

```python
l1 = ["banana","APPLE", "Watermelon"]
l2 = sorted(l1, key=str.lower)
print(l2)

# ['APPLE', 'banana', 'Watermelon']
```

### lambda

你注意到我们在上面使用了 `lambda` 来定义一个匿名函数，十分方便。如果你熟悉其它语言类似 JS 的话，可以把它理解成一个 callback 函数，参数名一一对应就行。

### cmp_to_key

在 python3 中，sorted 函数取消了自带的`cmp`函数，需要借助`functools` 库中的 `cmp_to_key`来做比较。
比如如果要按照数组元素的绝对值来排序：

```
from functools import cmp_to_key
def absSort(arr):
    newarr = sorted(arr, key = cmp_to_key(sortfunc))
    return newarr
def sortfunc(a, b):
    if abs(a) < abs(b):
      return -1
    elif abs(a) > abs(b):
      return 1
    else:
      return a - b
```

## set

set 的查找操作复杂度为`O(1)`，有时候可以替代`dict` 来存储中间过程。

- `add` : set 的添加是 `add` 不是`append`

- `remove` vs `discard`: 都是删除操作，区别在于`remove`不存在的元素会报错，`discard`不会。
- `union`, `intersection`: 快速获得并集和交集，方便一些去重操作。

## dict

字典，相当于其它语言中的`map`, `hashtable`, `hashmap`之类的，读取操作也是`O(1)` 复杂度

### keys(), values(), items()

这三个方法可以分别获得`key`, `value`, `{key: value}`的数组。

### setdefault

这个函数经常在初始化字典时候使用，如果某个`key`在字典中存在，返回它的`value`, 否则返回你给的 default 值。比如在建一个 trie 树的时候

```python
node = self.root
for char in word:
    node = node.setdefault(char, {})
```

### OrderedDict

OrderedDict 能记录你 key 和 value 插入的顺序，底层其实是一个双向链表加哈希表的实现。我们甚至可以使用`move_to_end`这样的函数：

```python
>>> d = OrderedDict.fromkeys('abcde')
>>> d.move_to_end('b')
>>> ''.join(d.keys())
'acdeb'
# 放开头
>>> d.move_to_end('b', last=False)
>>> ''.join(d.keys())
'bacde'
```

### defaultdict

`defaultdict`可以很好地来解决一些初始化的问题，比如 value 是一个 list，每次需要判断 key 是否存在的情况。这时我们可以直接定义

```python
d = defaultdict(list)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in s:
     d[k].append(v)
sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

## heapq

heapq 就是 python 的 priority queue，`heapq[0]`即为堆顶元素。

heapq 的实现是小顶堆，如果需要一个大顶堆，常规的一个做法是把值取负存入，取出时再反转。
以下是借助 heapq 来实现 heapsort 的例子：

```
>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## bisect

python 自带二分查找的库，在一些不要求实现 binary search，但是借助它能加速的场景下可以直接使用。

```python
bisect.bisect(a, x, lo=0, hi=len(a))
这里的参数分别为 数组，要查找的数，范围起始点，范围结束点
```

相似函数还有

- `bisect.bisect_left`
- `bisect.bisect_right`
  分别返回可以插入 x 的最左和最右 index

## Counter

Counter 接受的参数可以是一个 string, 或者一个 list, mapping

```
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
```

- `most_common(n)`
  可以得到出现次数最多的 n 个数：

```
>>> Counter('abracadabra').most_common(3)  # doctest: +SKIP
[('a', 5), ('r', 2), ('b', 2)]
```

## strings

### ord, char

ord 返回单个字符的 unicode:

```
>>> ord('a')
97
```

char 则是反向操作：

```
>>> chr(100)
'd'
```

### strip

移除 string 前后的字符串，默认来移除空格，但是也可以给一个字符串，然后会移除含有这个字符串的部分：

```py
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
```

### split

按照某个字符串来切分，返回一个 list, 可以传入一个参数`maxsplit`来限定分离数。

```
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
```

## int/ float

### 最大, 最小 number

有时候初始化我们需要设定 `Math.max()` 和 `Math.min()`, 在 python 中分别以 `float('inf')` 和 `float('-inf')`表示

在 python2 中我们也可以这么做：

```
import sys

#maxint
Max = sys.maxint
```

### 除法

在 python3 中， `/` 会保留浮点，相当于 float 相除，如果需要做到像 pyhton2 中的 int 相除，需要 `//`：

```py
>>> 3 / 2
1.5
>>> 3 // 2
1
```

### 次方

在 python 中为 `**`:

```
>>> 2 ** 10
1024
```

## conditions

在 python 的三项表达式(ternary operation) 与其它语言不太一样：

```
res = a if condition else b
```

它表示如果 condition 满足，那么 `res = a`, 不然 `res = b`，在类 c 的语言里即为：

```
res = condition ? a : b;
```

## any, all

`any(), all()`很好理解，就是字面意思，即参数中任何一个为 true 或者全部为 true 则返回 true。经常可以秀一些骚操作:
比如 [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) 这题：

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[x for x in y if x != '.'] for y in board]
        col = [[x for x in y if x != '.'] for y in zip(*board)]
        pal = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != '.'] for i in (0, 3, 6) for j in (0, 3, 6)]
        return all(len(set(x)) == len(x) for x in (*row, *col, *pal))
```

## itertools

这是 python 自带的迭代器库，有很多实用的、与遍历、迭代相关的函数。

### permutations 排列

```py
permutations('ABCD', 2)
# AB AC AD BA BC BD CA CB CD DA DB DC
```

### combinations 组合

```py
combinations('ABCD', 2)
# AB AC AD BC BD CD
```

### groupby 合并

https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby/322898

```
[k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
```

## functools

这个库里有很多高阶函数，包括前面介绍到的`cmp_to_key` 以及 `reduce`，但是比较逆天的有 `lru_cache`，即 least recently used cache. 这个 [LRU Cache](https://leetcode.com/problems/lru-cache/)是一个常见的面试题，通常用 hashmap 和双向链表来实现，python 居然直接内置了。

用法即直接作为 decorator 装饰在要 cache 的函数上，以变量值为 key 存储，当反复调用时直接返回计算过的值，例子如下：

### lru_cache

https://leetcode.com/problems/stone-game-ii/discuss/345230/Python-DP-Solution

```py
  def stoneGameII(self, A: List[int]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N: return A[i]
            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)
```

## resource

- 这是一个大神用各种 Python trick 解题的 repo，可供娱乐：

  > https://github.com/cy69855522/Shortest-LeetCode-Python-Solutions

- 另一个关于各种 python tricks 的总结：
  > https://github.com/brennerm/PyTricks

当然 Leetcode 讨论区还会经常见到 `StefanPochmann` 或者 `lee215`这样的大神 Po 一些很秀技的 python 代码，都是学习范本。
