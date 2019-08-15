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
var reverseList = function(head) {
  var newHead = null;
  var next;
  while (head !== null) {
    next = head.next;
    head.next = newHead;
    newHead = head;
    head = next;
  }
  return newHead;
};
/**
 *
 * @param {ListNode} head
 */
var reverseList_recursive = function(head) {
  // end condition
  if (!head || !head.next) {
    return head;
  }
  const end = reverseList(head.next);
  head.next.next = head;
  head.next = null;
  return end;
};
