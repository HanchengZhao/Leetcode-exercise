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
    
    var tempLL = new ListNode(-1);
    tempLL.next = head;
    var front_pointer = tempLL;
    var arr = [];
    for(var i = 0; i < m - 1; i++){
        front_pointer = front_pointer.next;
    }//go to m
    var rear_pointer = front_pointer.next;
    for(var j = 0; j < n - m ; j++ ){
        arr.unshift(rear_pointer);
        rear_pointer = rear_pointer.next;
    }// get a reversed order array in arr
    rear_pointer = rear_pointer.next;//one element after n
    
    var reversedLL_head = new ListNode(arr[0]);
    var reversedLL = reversedLL_head;
    for (var k = 1; k < n - m ; k++ ) {
        reversedLL.next = arr[i];
        reversedLL = reversedLL.next;
    }
    
    front_pointer.next = reversedLL_head;
    reversedLL.next = rear_pointer;
    
    return tempLL.next;
    
};