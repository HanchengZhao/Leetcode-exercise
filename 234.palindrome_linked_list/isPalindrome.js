/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var arr = [];
    var curr = head;
    while (curr !== null){
        arr.push(curr.val);
        curr = curr.next;
    }
    
    var sec = head;
    while(sec !== null){
        var val = arr.pop();
        if(val !== sec.val) return false;
        sec = sec.next;
    }
    if(arr.length !== 0) return false;
    return true;
    
};