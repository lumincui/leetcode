"""
19. Remove Nth Node From End of List - 删除链表的倒数第 N 个结点
难度: Medium | 类型: linked_list
链接: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

题目描述:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1:
输入: head = [1,2,3,4,5], n = 2
输出: [1,2,3,5]

示例 2:
输入: head = [1], n = 1
输出: []

示例 3:
输入: head = [1,2], n = 1
输出: [1]

约束:
- 链表中结点的数目为 sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(val=-1, next=head)
    slow, fast = dummy, dummy
    steps = n
    while fast and steps >= 0:
        fast = fast.next
        steps = steps - 1

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


# ===================== 测试工具 =====================
def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def to_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals

def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ]
    
    passed = 0
    for i, (vals, n, expected) in enumerate(test_cases):
        head = make_list(vals)
        result_head = removeNthFromEnd(head, n)
        result_vals = to_list(result_head)
        
        if result_vals == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: vals={vals}, n={n}\n    expected={expected}\n         got={result_vals}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
