/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;
        Map<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        //copy the value
        RandomListNode node = head;
        while (node != null) {
            map.put(node, new RandomListNode(node.label));
            node = node.next;
        }

        //copy the reference
        node = head;
        while (node != null) {
            if (node.next != null) {
                map.get(node).next = node.next;
            }
            if (node.random != null) {
                map.get(node).random = node.random;
            }
            node = node.next;
        }
        return map.get(head);
    }
}