from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __iter__(self):
        current = self
        while current:
            yield (current.val, current.random.val if current.random else None)
            current = current.next
        

def arr2list(l: list) -> Optional[Node]:
    if not l: return None
    list_nodes = []
    for node_info in l:
        list_nodes.append(Node(x=node_info[0]))
    list_nodes.append(None)
    
    for index in range(len(list_nodes)-1):
        node = list_nodes[index]
        node.next = list_nodes[index+1]
    

        random_index = l[index][1] if l[index][1] is not None else -1
        node.random = list_nodes[random_index]
    
    return list_nodes[0]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_map = {None: None}
        current = head
        while current:
            new_node = Node(x=current.val)
            list_map[current] = new_node
            current = current.next
        
        current = head
        while current:
            list_map[current].next = list_map[current.next]
            list_map[current].random = list_map[current.random]
            current = current.next
        return list_map[head]

if __name__ == "__main__":
    head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head  = arr2list(head)
    print([node for node in Solution().copyRandomList(head)])
    head = [[1,1],[2,1]]
    head  = arr2list(head)
    print([node for node in Solution().copyRandomList(head)])
    head = [[3,None],[3,0],[3,None]]
    head  = arr2list(head)
    print([node for node in Solution().copyRandomList(head)])