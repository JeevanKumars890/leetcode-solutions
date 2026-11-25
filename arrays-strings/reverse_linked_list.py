class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Helpers for testing
def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

# Tests
print(to_list(reverse_list(build([1, 2, 3, 4, 5]))))  # typical case, expect [5, 4, 3, 2, 1]
print(to_list(reverse_list(build([]))))               # edge case: empty list, expect []