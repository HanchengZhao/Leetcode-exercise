/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	fast := head
	slow := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			// find the intersection
			for head != slow {
				head = head.Next
				slow = slow.Next
			}

			return head
		}
	}
	return nil
}