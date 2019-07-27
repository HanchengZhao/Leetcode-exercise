class ListNode {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  this.cap = capacity;
  this.map = {};
  this.head = new ListNode(0, 0);
  this.tail = new ListNode(0, 0);
  this.head.next = this.tail;
  this.tail.prev = this.head;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  if (key in this.map) {
    node = this.map[key];
    this._remove(key);
    this._addToHead(key, node.value);
    return node.value;
  } else {
    return -1;
  }
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  // if existed, change the value
  if (this.get(key) !== -1) {
    let node = this.map[key];
    node.value = value;
  } else {
    // reach the cap, remove the first element
    if (Object.keys(this.map).length === this.cap) {
      let firstNode = this.head.next;
      this._remove(firstNode.key);
    }
    this._addToHead(key, value);
  }
};

LRUCache.prototype._remove = function(key) {
  let node = this.map[key];
  let prev = node.prev;
  let next = node.next;
  if (prev !== null) prev.next = next;
  if (next !== null) next.prev = prev;
  delete this.map[key];
};

LRUCache.prototype._addToHead = function(key, value) {
  let newNode = new ListNode(key, value);
  let last = this.tail.prev;
  last.next = newNode;
  newNode.prev = last;
  newNode.next = this.tail;
  this.tail.prev = newNode;
  this.map[key] = newNode;
};
/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
//  */
// var obj = new LRUCache(2);
// var param_1 = obj.get(1);
// obj.put(1, 1);
// obj.put(2, 2);
// obj.put(3, 3);
// console.log(obj);
