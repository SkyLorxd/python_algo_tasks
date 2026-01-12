from tasks.data_stuctures.double_connected_node.solution import solution, DoubleConnectedNode


def build_list(values):
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0], nodes


def collect_forward(head):
    result = []
    cur = head
    while cur:
        result.append(cur.value)
        cur = cur.next
    return result


def collect_backward(tail):
    result = []
    cur = tail
    while cur:
        result.append(cur.value)
        cur = cur.prev
    return result


def test_from_example():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    new_head = solution(node0)

    assert new_head is node3
    assert collect_forward(new_head) == ["node3", "node2", "node1", "node0"]


def test_single_element():
    node = DoubleConnectedNode(1)
    new_head = solution(node)

    assert new_head is node
    assert new_head.next is None
    assert new_head.prev is None


def test_two_elements():
    head, nodes = build_list([1, 2])
    new_head = solution(head)

    assert collect_forward(new_head) == [2, 1]
    assert new_head.prev is None
    assert new_head.next.value == 1
    assert new_head.next.prev is new_head


def test_multiple_elements():
    head, _ = build_list([1, 2, 3, 4, 5])
    new_head = solution(head)

    assert collect_forward(new_head) == [5, 4, 3, 2, 1]


def test_large_list():
    n = 1000
    head, _ = build_list(list(range(n)))
    new_head = solution(head)

    assert collect_forward(new_head) == list(reversed(range(n)))
