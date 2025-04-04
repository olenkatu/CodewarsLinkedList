class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if source is None:
        raise TypeError
    el = source.data
    source = source.next
    new_dest = Node(el)
    new_dest.next = dest
    return Context(source, new_dest)
