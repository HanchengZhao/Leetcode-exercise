'''
https://www.1point3acres.com/bbs/thread-548370-1-1.html

两道题
1.  找没有父母的孩子+找只有一个parent的孩子
题目跟第二题一样，只是返回的东西不一样
2. check ‍‍‍‍‌‍‍‌‍‌‍‍‌‍‌‌‌whether two children have common ancestors
/*

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
\ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parentChildPairs1, 3, 8) => false
hasCommonAncestor(parentChildPairs1, 5, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 9) => true
hasCommonAncestor(parentChildPairs1, 1, 3) => false
hasCommonAncestor(parentChildPairs1, 7, 11) => true
hasCommonAncestor(parentChildPairs1, 6, 5) => true
hasCommonAncestor(parentChildPairs1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
\ /    /  \
  3    6   7
   \        \
    4        8

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

hasCommonAncestor(parentChildPairs2, 4, 12) => true
hasCommonAncestor(parentChildPairs2, 1, 6) => false
hasCommonAncestor(parentChildPairs2, 1, 12) => false
*/

same as: https://www.1point3acres.com/bbs/interview/pinterest-software-engineer-319606.html
'''
parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

# question 1


def find_children_with_0_and_1_parent(pairs):
    from collections import Counter
    parents = []
    children = []
    for p in pairs:
        parents.append(p[0])
        children.append(p[1])
    c = Counter(children)
    n_parents = {}
    for i in set(parents) | set(children):
        if i in c:
            n_parents[i] = c[i]
        else:
            n_parents[i] = 0
    return [[i for i in n_parents.keys() if n_parents[i] == 0], [i for i in n_parents.keys() if n_parents[i] == 1]]


# print(find_children_with_0_and_1_parent(parentChildPairs1))

# question 2

def findAllParents(pairs, node):
    parents = []
    for p in pairs:
        if p[1] == node:
            parents.append(p[0])
    next_parents = []
    for i in parents:
        next_parents += findAllParents(pairs, i)
    return parents + next_parents


def findCommonParents(pairs, a, b):
    a_parents = findAllParents(pairs, a)
    b_parents = findAllParents(pairs, b)
    # print(a_parents, b_parents)
    return True if set(a_parents) & set(b_parents) else False


print(findCommonParents(parentChildPairs1, 5, 8))

# question 3


def findParentsWithDepth(pairs, node, depth=0):
    parents = []
    for p in pairs:
        if p[1] == node:
            parents.append([p[0], depth])
    next_parents = []
    for i in parents:
        next_parents += findParentsWithDepth(pairs, i[0], depth + 1)
    return parents + next_parents


def getFurthestParent(pairs, node):
    parents = findParentsWithDepth(pairs, node)
    if not parents:
        return None
    parents.sort(key=lambda p: p[1])
    print(parents)
    # return the last one
    return parents[-1][0]


print(getFurthestParent(parentChildPairs1, 6))
