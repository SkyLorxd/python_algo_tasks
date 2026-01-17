class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node: Node):
    cur = node
    while cur:
        print(cur.value)
        cur = cur.next_item
