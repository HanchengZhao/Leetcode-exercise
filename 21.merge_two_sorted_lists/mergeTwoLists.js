/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var dummy = new ListNode(-1);
    // dummy.next = (l1 > l2) ? l1 : l2;
    var head = dummy;
    while(l1 !== null && l2 !== null){
        if (l1.val > l2.val){
            head.next = l2;
            l2 = l2.next;
            head = head.next;
        }else{
            head.next = l1;
            l1 = l1.next;
            head = head.next;
        }
    }
    if (l1 === null){
        head.next = l2;
    }else{
        head.next = l1;
    }
    return dummy.next;
};