from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        node = head
        while node:
            if node not in nodes:
                nodes.add(node)
                node = node.next
            else:
                return True
        return False


if __name__ == "__main__":
    # [3,2,0,-4]
    t = ListNode(3)
    t.next = ListNode(2)
    t.next.next = ListNode(0)
    t.next.next.next = ListNode(-4)
    t.next.next.next.next = t.next

    #condition = bool(t.next == t.next.next.next.next)
    #print(condition)
    print(Solution().hasCycle(t))