# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def _nodes_to_list(head):
    pass

def _list_to_nodes(l):
    if not l: return ListNode(0)
    head = ListNode(l[0])
    curr_node = head
    for i in range(1, len(l)):
        temp = ListNode(l[i])
        curr_node.next = temp
        curr_node = curr_node.next
    return head

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            node = node.next
        #import pdb; pdb.set_trace()
        node.val = 0


if __name__ == "__main__":
    l = [4,5,1,9]
    head = _list_to_nodes(l)
    print([head.val, head.next.val, head.next.next.val, head.next.next.next.val])
    Solution().deleteNode(head.next)
    print([head.val, head.next.val, head.next.next.val, head.next.next.next.val])