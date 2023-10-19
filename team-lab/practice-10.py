# 問題10: データ構造とアルゴリズム
# 連結リストやツリー構造（二分木など）を操作するプログラムを実装してください。例えば、連結リスト内の逆順の要素を取得する、二分探索木から指定された値を探すなどの操作を含めます。

class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

reverse_list = reverse_linked_list(node1)
current = reverse_list

while current is not None:
    print(current.value, end=">")
    current = current.next


