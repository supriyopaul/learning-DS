from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next


def list2linked(nums: List):
    if not nums: return None
    head = ListNode(nums[0])
    tmp_node = head
    for index, num in enumerate(nums):
        if index == 0: continue
        node = ListNode(num)
        tmp_node.next = node
        tmp_node = tmp_node.next
    return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return
        if not list1 and list2: return list2
        if not list2 and list1: return list1

        node1 = list1
        node2 = list2
        first_node = node1 if node1.val <= node2.val else node2

        if first_node == node1:
            merged = ListNode(node1.val)
            node1 = node1.next
        else:
            merged = ListNode(node2.val)
            node2 = node2.next
        
        first_node = merged

        while (node1 and node2):
            if node1.val >= node2.val:
                merged.next = ListNode(node2.val)
                node2 = node2.next

            else:
                merged.next = ListNode(node1.val)
                node1 = node1.next

            merged = merged.next
            
            

        if node2 and not node1:
            while node2:
                merged.next = node2
                node2 = node2.next
                merged = merged.next

        if not node2 and node1:
            while node1:
                merged.next = node1
                node1 = node1.next
                merged = merged.next
        
        return first_node
        
if __name__ == "__main__":
    list1 = list2linked([1,2,4])
    list2 = list2linked([1,3,4])
    print([ i for i in Solution().mergeTwoLists(list1, list2)])
    list1 = list2linked([2])
    list2 = list2linked([1])
    print([ i for i in Solution().mergeTwoLists(list1, list2)])
