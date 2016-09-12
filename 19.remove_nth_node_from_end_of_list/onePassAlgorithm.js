/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
function ListNode(val){
    this.val = val;
    this.next = null;
}
var removeNthFromEnd = function(head, n) {
    var dummyNode = new ListNode(-1);
    dummyNode.next = head;
    var first = dummyNode; 
    var second = dummyNode;
    for(var i = 0; i < n ; i++){
        first = first.next;
    }
    while(first.next !== null){
        first = first.next;
        second = second.next;
    }
    var deleteNode = second.next;
    second.next = deleteNode.next;
    return dummyNode.next;
};