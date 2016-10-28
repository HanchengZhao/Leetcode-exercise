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
    var len = 1;
    var tail = head;
    var newhead = head;
    while(tail.next){
        tail = tail.next;
        len++;
    }
    
    if(k %= len){
        tail.next = head;//make a circle here
        for(var i = 0; i < len-k; i++ ){
            tail = tail.next;
        }
        newhead = tail.next;
        tail.next = null;//break the circle
    }
    
    return newhead;
};