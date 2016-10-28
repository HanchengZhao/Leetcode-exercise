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
    if (head === null || head.next === null) return head;
    var dummy = new ListNode(-1);
    dummy.next = head;
    var pre = dummy;
    var cur = head;
    while (cur != null){
        while (cur.next !== null && cur.val === cur.next.val) { //remove the duplicates from start
            cur = cur.next;
        }
        if(pre.next == cur){
            pre = pre.next;
        }else{
            pre.next = cur.next;
        }
        cur = cur.next;
    }   
    return dummy.next;
};