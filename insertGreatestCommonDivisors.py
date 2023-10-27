from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_hcf(a, b):
    smaller_num, larger_num = min(a, b), max(a,b)
    common_divisors = list()
    divisor = 1
    while divisor <= smaller_num:
        if smaller_num%divisor == 0 and larger_num%divisor == 0:
            common_divisors.append(divisor)
        divisor += 1
    return max(common_divisors)

def link_nodes(node1, node2, node3):
    node1.next = node2
    node2.next = node3

def create_list(nums):
    head = ListNode(nums[0])
    node =  head
    i = 1
    while i < len(nums):
        next = ListNode(nums[i])
        node.next = next
        node = next
        i += 1
    return head

def print_list(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    print(l)
    


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        left = head
        right = head.next
        
        while right:
            hcf = get_hcf(left.val, right.val)
            hcf_node = ListNode(hcf)
            link_nodes(left, hcf_node, right)
            left = right
            right = right.next
        return head


if __name__ == "__main__":
    print(get_hcf(18, 6))
    print(get_hcf(10, 6))
    print(get_hcf(10, 3))
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    link_nodes(node1,node2,node3)
    print(node1.val, node1.next.val, node1.next.next.val)
    head = create_list([18, 6, 10, 3])
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
    print_list(head)
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
    print_list(Solution().insertGreatestCommonDivisors(head))
    #print_list(Solution().insertGreatestCommonDivisors(head))
