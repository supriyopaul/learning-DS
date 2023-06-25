from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodes2list(head: Optional[ListNode]) -> list:
    if not head: return []
    curr_node = head
    result = []
    while curr_node:
        result.append(curr_node.val)
        curr_node = curr_node.next if curr_node.next is not None else None
    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return head.next
        ll_len = len(nodes2list(head))
        start_index = 0
        end_index = 1
        index_to_remove = ll_len - n
        if index_to_remove == 0: return head.next
        start_node = head
        end_node = head.next
        while end_node:
            #import pdb; pdb.set_trace()
            if not end_index == index_to_remove:
                start_index = end_index
                end_index += 1
                start_node = end_node
                end_node = end_node.next
            else:
                start_node.next = end_node.next
                return head

if __name__ == "__main__":
    # head = [1,2,3,4,5], n = 2
    a = ListNode(val=5)
    b = ListNode(val=4, next=a)
    c = ListNode(val=3, next=b)
    d = ListNode(val=2, next=c)
    head  = ListNode(val=1, next=d)
    print(nodes2list(head))
    new_head = Solution().removeNthFromEnd(head, 2)
    print(nodes2list(new_head))