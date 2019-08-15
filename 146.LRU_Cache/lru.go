package LRU_Cache

type Node struct {
	// used for map to track
	key   int
	value int
	prev  *Node
	next  *Node
}

// keyMap here is used to reduce find complexity to O(1), and track the length of list
type LRUCache struct {
	capacity int
	head     *Node
	tail     *Node
	keyMap   map[int]*Node
}

func (this *LRUCache) add(n *Node) {
	last := this.tail.prev
	last.next = n
	this.tail.prev = n
	// points this node to the last and tail
	n.prev = last
	n.next = this.tail
}

func (this *LRUCache) remove(n *Node) {
	prev := n.prev
	next := n.next
	// modify pointer from last and tail to this node
	if n.prev != nil {
		n.prev.next = next
	}
	if n.next != nil {
		n.next.prev = prev
	}
}

func Constructor(capacity int) LRUCache {
	var cache LRUCache
	cache.capacity = capacity
	cache.head.next = cache.tail
	cache.tail.prev = cache.head
	return cache
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.keyMap[key]; ok {
		// put the node at the end of the list
		this.remove(node)
		this.add(node)
		return node.value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	_, ok := this.keyMap[key]
	if ok != false {
		delete(this.keyMap, key)
	}
	n := Node{key: key, value: value}
	this.add(&n)
	this.keyMap[key] = &n
	if len(this.keyMap) > this.capacity {
		firstNode := this.head.next
		this.remove(firstNode)
		delete(this.keyMap, firstNode.key)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
