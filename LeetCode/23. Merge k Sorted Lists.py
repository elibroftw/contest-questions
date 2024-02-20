# if you know what a heapq is, then this is a Medium problem
# if you don't know what a heapq is, you would end up using a lot of compute
#   on finding the minimum from k-list before pushing

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq


# for other languages with a heapq helper, you should use a tuple (value, UUID, node) to break ties
# alternatively, a HeapNode like this works too
# Or you can use implement the comparison trait in Rust and get away with it?
# of course you can roll your own heap queue structure if you understand how to represent a tree as an array

class HeapNode:
    def __init__(self, node):
        self.node = node

    @property
    def val(self):
        return self.node.val

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        return_node = None
        last_node = return_node
        lists = [l for l in lists if l != None]
        heapq.heapify(lists)
        while lists:
            node = heapq.heappop(lists)
            new_node = ListNode(node.val)
            if return_node is None:
                return_node = new_node
            else:
                last_node.next = new_node
            last_node = new_node
            if node.next is not None:
                heapq.heappush(lists, node.next)
            r = len(lists) == 0

        return return_node
