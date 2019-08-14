from collections import defaultdict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class dLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)  # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node

# use one dlinkedlist to store all the nodes
# then use


class LFUCache:

    def __init__(self, capacity: int):

        self._size = 0
        self._capacity = capacity

        self._node = dict()  # key: Node
        self._freq = defaultdict(dLinkedList)
        self._minFreq = 0

    def _update(self, node):
        """ 
        This is a helper function that used in the following two cases:

            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.

        The common point of these two cases is that:

            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change

        The logic of this function is:

            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`

        All of the above opeartions took O(1) time.
        """
        freq = node.freq

        self._freq[freq].pop(node)
        if self._minFreq == freq and not self._freq[freq]:
            self._minFreq += 1
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key: int) -> int:

        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.

        Otherwise, the following logic will be performed

        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1

        (*) How to pop the least frequently used item? Two facts:

        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)

        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...

        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity == 0:
            return
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minFreq].pop()
                del self._node[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minFreq = 1
            self._size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
