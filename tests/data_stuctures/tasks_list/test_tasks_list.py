import sys
import io
from tasks.data_stuctures.tasks_list.solution import Node, solution


def capture_output(fn):
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        fn()
        return buffer.getvalue()
    finally:
        sys.stdout = old_stdout


def test_single_node():
    node = Node("A")
    out = capture_output(lambda: solution(node))
    assert out == "A\n"


def test_two_nodes():
    node1 = Node("B")
    node0 = Node("A", node1)
    out = capture_output(lambda: solution(node0))
    assert out == "A\nB\n"


def test_example_from_task():
    node3 = Node("node3")
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    out = capture_output(lambda: solution(node0))
    assert out == "node0\nnode1\nnode2\nnode3\n"


def test_numeric_values():
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    out = capture_output(lambda: solution(node1))
    assert out == "1\n2\n3\n"


def test_large_list_5000():
    head = Node(0)
    cur = head
    for i in range(1, 5000):
        cur.next_item = Node(i)
        cur = cur.next_item

    out = capture_output(lambda: solution(head))
    lines = out.splitlines()

    assert len(lines) == 5000
    assert lines[0] == "0"
    assert lines[-1] == "4999"
