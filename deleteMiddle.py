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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None

        slow, fast = head, head
        prev = slow
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        print(prev.val, slow.val)

        prev.next = slow.next
        del slow
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    sol1 = Solution().deleteMiddle(head=head) #[1,2,4]

    head = ListNode(2)
    head.next = ListNode(1)
    sol2 = Solution().deleteMiddle(head=head) #[2]

    head = ListNode(1)
    sol2 = Solution().deleteMiddle(head=head) #[]

    print([node for node in sol1])
    print([node for node in sol2])