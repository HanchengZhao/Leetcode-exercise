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
    let dummy = new ListNode(-1);
    dummy.next = head;
    let pre = dummy;
    for (let i=0;i<m-1;i++) pre = pre.next;
    let revHead = pre.next, then = revHead.next;
    for (let i=0;i<n-m;i++){
        revHead.next = then.next;
        then.next = pre.next;
        pre.next = then;
        then = revHead.next;
    }
    return dummy.next;
};


