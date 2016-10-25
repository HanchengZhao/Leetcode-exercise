/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    if(headA === null || headB === null) return null;
    var pointerA = headA;
    var pointerB = headB;
    var lenA = 0, lenB = 0;
    var dif;
    while(pointerA.next !== null){//get the length of A
        pointerA = pointerA.next;
        lenA++;
    }
    while(pointerB.next !== null){//get the length of B
        pointerB = pointerB.next;
        lenB++;
    }
    if(lenA > lenB){
        dif = lenA - lenB;
        for(let i = 0; i< dif; i++){
            headA = headA.next;
        }
    }
    if(lenA < lenB){
        dif = lenB - lenA;
        for(let i = 0; i< dif; i++){
            headB = headB.next;
        }
    }
    while(headA != headB){
        headA = headA.next;
        headB = headB.next;
    }
    return headA;
};