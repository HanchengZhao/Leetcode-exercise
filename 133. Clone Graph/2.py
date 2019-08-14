# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = []
        dic = {}
        queue.append(node)
        while queue:
            n = queue.pop(0)
            dic[n] = UndirectedGraphNode(n.label)
            for i in n.neighbors:
                if i not in dic:
                    queue.append(i)
        for ori in dic.keys():
            cur = dic[ori]
            for n in ori.neighbors:
                cur.neighbors.append(dic[n])
        return dic[node]