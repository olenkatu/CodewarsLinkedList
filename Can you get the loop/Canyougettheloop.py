def loop_size(node):
    slow = node
    fast = node
    
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    fast = fast.next
    while fast != slow:
        count += 1
        fast = fast.next
        
    return count