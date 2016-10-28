/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (head === null || head.next === null || k === 0) return head;
    var newhead;
    var fast = head;
    var slow = head;
    for(var i = 0; i < k; i++){
        if(fast.next === null){ //rotate back to head
            fast = head;
        }else{
            fast = fast.next;
        }
    }
    while(fast.next !== null){//slow now reaches the node to be shifted
        fast = fast.next;
        slow = slow.next;
    }
    fast.next = head;
    newhead = slow.next;
    slow.next = null;
    return newhead;
};