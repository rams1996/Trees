/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;
​
    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }
​
    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
​
class Solution {
    public Node connect(Node root) {
        Node queue = root;
    while (queue != null) {
        Node level = new Node(0);
        Node current = level;
        while (queue != null) {
            if (queue.left != null) {
                current.next = queue.left;
                current = current.next;
            }
            if (queue.right != null) {
                current.next = queue.right;
                current = current.next;
            }
            queue = queue.next;
        }
        queue = level.next;
    }
        return root;
    }
}
