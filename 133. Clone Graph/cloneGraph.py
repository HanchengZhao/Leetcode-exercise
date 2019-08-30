class UndirectedGraphNode:
    def __init__(self, x):
        self.lable = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        queue = [] # used for bfs
        map = {} # store node info, key is original node and value is the new node
        queue.append(node)
        # step 1: copy all the nodes
        while queue:
            curr = queue.pop(0)
            copy = UndirectedGraphNode(curr.label)
            map[curr] = copy 
            for n in curr.neighbors:
                if n not in map: # skip all visited nodes
                    queue.append(n)
        # step 2: copy connections between them
        for ori in map.keys():
            copy = map[ori]
            for nei in ori.neighbors: # not copy.neighbors = ori.neighbours because we have to add new Nodes, rather than old ones
                copy.neighbors.append(map[nei])
        return map[node]


'''
step 1: copy all the nodes
step 2: copy connections between them
'''
