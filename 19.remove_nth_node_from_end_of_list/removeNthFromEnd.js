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
    var dummyNode2 = dummyNode;
    var length = 1;
    //get the length of the list code
    while(dummyNode2.next !== null){
        dummyNode2 = dummyNode2.next;
        length++;
    }
    var dummyNode3 = dummyNode;
    for(var i=0; i < length - n - 1 ; i++){
        dummyNode3 = dummyNode3.next;
    }
    var deleteNode = dummyNode3.next;
    dummyNode3.next = deleteNode.next;
    return dummyNode.next;
};