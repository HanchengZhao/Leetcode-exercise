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
var detectCycle = function(head) {
    if(head === null) return null;
    var slow = head;
    var fast = head;
    while(fast.next!==null && fast.next.next !== null){
        slow = slow.next;
        fast = fast.next.next;
        if(fast === slow){//the cycle exists
            while(head !== slow){
                head = head.next;
                slow = slow.next;
            }
            return head;
        }
    }
    return null;
};


// Definitions:
// Cycle = length of the cycle, if exists.
// C is the beginning of Cycle, S is the distance of slow pointer from C when slow pointer meets fast pointer.

// Distance(slow) = C + S, Distance(fast) = 2 * Distance(slow) = 2 * (C + S). To let slow poiner meets fast pointer, only if fast pointer run n cycle more than slow pointer. Distance(fast) - Distance(slow) = Cycle
// => 2 * (C + S) - (C + S)	= nCycle
// =>	C + S = nCycle
// =>	C = nCycle - S= (n-1)Cycle + cycle-S