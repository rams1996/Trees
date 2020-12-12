"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        temp=root
        parent=root
        while(temp.left):
            parent=temp
            while(parent):
                parent.left.next=parent.right
                if parent.next:
                    parent.right.next=parent.next.left
                parent=parent.next
            temp=temp.left
        return root
            
        
