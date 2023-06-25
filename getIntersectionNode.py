from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB
        nodesA = set()
        nodesB = set()
        while nodeA:
            nodesA.add(nodeA)
            nodeA = nodeA.next
        while nodeB:
            if nodeB not in nodesA:
                nodesB.add(nodeB)
            else:
                return nodeB
            nodeB = nodeB.next

if __name__ == "__main__":
    #Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    #Output: Reference of the node with value = 8
    headC = ListNode(8)
    headC.next = ListNode(4)
    headC.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = headC

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headC

    solution = Solution()
    print(solution.getIntersectionNode(headA, headB).val) # 8
