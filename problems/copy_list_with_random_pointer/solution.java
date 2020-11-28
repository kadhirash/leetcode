/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Node copyRandomList(Node head) {
        Node curr = head;
        Node next = null;
        
        while (curr != null){
            next = curr.next;
            
            Node copy = new Node(curr.val);
            curr.next = copy;
            copy.next = next;
            
            curr = next;
        }
        curr = head;
        while(curr != null){
            if(curr.random !=null){
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        curr = head;
        Node dummyHead = new Node(0);
        Node cloneListTail = dummyHead;
        Node copy = null;
        
        while (curr != null){
            next = curr.next.next;
            copy = curr.next;
            
            cloneListTail.next = copy;
            cloneListTail = copy;
            
            curr.next = next;
            
            curr = next;
        }
        return dummyHead.next;
    }
}