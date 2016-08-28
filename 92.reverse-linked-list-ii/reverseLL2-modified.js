/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
function ListNode(val){
    this.val = val;
    this.next = null;
}

var reverseBetween = function(head, m, n) {
    if(head === null) return null;
    var dummy = new ListNode(-1);
    dummy.next = head;
    var pre = dummy;

    for(var i = 0; i < m - 1; i++) pre = pre.next; // get to 1 place before m
    var start = pre.next; //pointer to the beginning to the sublist needing reversed
    var then = start.next; // pointer to the node need reversed
    for(var j = 0; j < n - m; j++){
        // start node value does not change
        // pre does not change
        start.next = then.next; // skip then to next element  (Skip)
        then.next = pre.next; //set ref to the current first node in the reverse list (Set link)
        pre.next = then; // put the node at the 1st of list(Put node)
        then = start.next; // Move to next one (Move)
    }
    return dummy.next
    
};