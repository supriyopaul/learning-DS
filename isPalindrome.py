from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None

class Solution:
    def _make_list_doubly_linked(self, head):
        l = head
        r = head.next
        while r:
            print(r.val)
            r.prev = l
            l = r
            r = r.next
        return l
    
    def _list_in_reverse(self, tail):
        node = tail
        reverse_list = []
        while node:
            reverse_list.append(node.val)
            node = node.prev
        return reverse_list
    
    def _list(self, head):
        node = head
        _list = []
        while node:
            _list.append(node.val)
            node = node.next
        return _list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        tail = self._make_list_doubly_linked(head)
        return(self._list(head) == self._list_in_reverse(tail))




if __name__ == "__main__":
    head = ListNode(1) #[1,2,2,1]
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    head2 = ListNode(1) #[1,2]
    head2.next = ListNode(2)

    print(Solution().isPalindrome(head)) # True
    print(Solution().isPalindrome(head2)) # False