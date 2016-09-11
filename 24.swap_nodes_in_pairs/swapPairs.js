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
var swapPairs = function(head) {
    if(head === null || head.next === null) return head;
    var dummy = new ListNode(-1);
    dummy.next = head;
    var former = dummy;
    var first = head;
    var second = head.next;
    
    do {//use do sentence can solve the problem that there are only 2 elements to be swapped
         first.next = second.next;
        second.next = first;
        former.next = second;
        
        if(first.next !==null&&first.next.next !==null){//verify next element first and then the next
        former = first;
        first = former.next;
        second = first.next;
        }else{
           return dummy.next;
        }
    }
    
    while (second !== null);
    return dummy.next;
};