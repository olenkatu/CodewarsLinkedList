from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    try:
        if index < 0 or node is None:
            raise ArgumentException
        if index:
            for _ in range(index):
                node = node.next
        if node is None:
            raise ArgumentException
        return node
    except Exception:
        raise ArgumentException
 