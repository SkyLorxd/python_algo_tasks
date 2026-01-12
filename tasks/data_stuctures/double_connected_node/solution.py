class DoubleConnectedNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    current = node
    new_head = None

    while current:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev

    return new_head
