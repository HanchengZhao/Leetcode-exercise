/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    
    var dummy = new ListNode(-1);
    dummy.next = head;
    var current = head;
    while (current !== null && current.next !== null) {
        if (current.next.val === current.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return dummy.next;
};