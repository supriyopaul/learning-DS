from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __iter__(self):
        current = self
        while current is not None:
            yield current.val
            current = current.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val, fast.val)
        
        prev, current_node = None, slow.next
        while current_node:
            next_node = current_node.next
            current_node.next = prev

            prev = current_node
            current_node = next_node
        slow.next = None

        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next

        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    sol1 = Solution().reorderList(head=head) #[1,4,2,3]

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    sol2 = Solution().reorderList(head=head) #[1,5,2,4,3]

    print([node for node in sol1])
    print([node for node in sol2])