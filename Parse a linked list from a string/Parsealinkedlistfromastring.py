def linked_list_from_string(s):
    splitted = s.split(' -> ')[:-1]
    before = None
    for _ in range(len(splitted)):
        before = Node(int(splitted.pop()), before)
    return before
