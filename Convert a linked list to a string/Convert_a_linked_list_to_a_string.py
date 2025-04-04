def stringify(node):
    line = ''
    while True:
        try:
            line += str(node.data) + ' -> '
            node = node.next
        except AttributeError:
            break
    return line + 'None'