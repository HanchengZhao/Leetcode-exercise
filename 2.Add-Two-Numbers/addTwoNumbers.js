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
  function ListNode(val) {
     this.val = val;
     this.next = null;
 }
 
var addTwoNumbers = function(l1, l2) {
    var dummyList = new ListNode(0); // when refering to a linked list, we often refer to its node 
    var sumList = dummyList;
    var carry = 0, x, y,  sum; //x for value in l1, y for that in l2
    
    while(l1 !== null || l2 !== null || carry){
        x = (l1 !== null) ? l1.val : 0;
        y = (l2 !== null) ? l2.val : 0;
        sum = x + y + carry;
        carry = Math.floor(sum / 10);
        sumList.next = new ListNode(sum % 10);
        sumList = sumList.next
        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }
    // console.log(dummyList.next);
    // return dummyList.next;
    
    //put each element of the linked list into an array to meet Leetcode requirement
    var arr =[];
    for(var i = dummyList.next; i !== null; i = i.next){
        arr.unshift(i.next);
    }
    console.log(arr);
    return arr;
};