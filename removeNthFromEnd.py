from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        current = self
        while current:
            yield current.val
            current = current.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head

if __name__ == "__main__":
    # head = [1,2,3,4,5], n = 2
    a = ListNode(val=5)
    b = ListNode(val=4, next=a)
    c = ListNode(val=3, next=b)
    d = ListNode(val=2, next=c)
    head  = ListNode(val=1, next=d)
    Solution().removeNthFromEnd(head, 2)
    print([node for node in head])

    head  = ListNode(val=1)
    new_head = Solution().removeNthFromEnd(head, 1)

    head  = ListNode(val=1)
    head.next = ListNode(val=2)
    Solution().removeNthFromEnd(head, 2)
    print([node for node in head])