/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
function ListNode(val) {
     this.val = val;
     this.next = null;
};
var addTwoNumbers = function(l1, l2) {
    var dummyList = new ListNode(0);
    var curr = dummyList;
    var carry = 0, x, y, sum;
    while(l1 !== null || l2 !== null || carry){
    	x = (l1 !== null) ? l1.val : 0;
    	y = (l2 !== null) ? l2.val : 0;
    	sum = carry + x + y;
    	carry = Math.floor(sum / 10);  
    	curr.next = new ListNode(sum % 10);
    	curr = curr.next;
    	if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    } 
    // return dummyList.next;
    
    //put each element of the linked list into an array
    var arr =[];
    for(var i = dummyList.next; i !== null; i = i.next){
        arr.push(i.val);
    }
    // console.log(arr);
    return arr;
};