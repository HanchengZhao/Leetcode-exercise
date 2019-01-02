/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package linkedlist

type ListNode struct {
	Val  int
	Next *ListNode
}

// iterative
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	var nxt *ListNode
	curt := head
	for curt != nil {
		nxt = curt.Next
		curt.Next = prev
		prev = curt
		curt = nxt
	}
	return prev
}

//recursive
// pass the end node all the way to the beginning,
// in the meantime, reverse the link
func reverseList2(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	end := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return end
}
