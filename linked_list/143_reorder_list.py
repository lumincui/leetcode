'''
143. Reorder List
难度: Medium | 类型: linked_list
链接: https://leetcode.com/problems/reorder-list/

题目描述:
    给定一个单链表 L0 -> L1 -> ... -> Ln-1 -> Ln，
    将其重排为：L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
    不能只改变节点值，必须实际交换节点。

示例:
    输入: head = [1,2,3,4]
    输出: [1,4,2,3]

    输入: head = [1,2,3,4,5]
    输出: [1,5,2,4,3]

约束:
    - 链表节点数量范围 [1, 5 * 10^4]
    - 1 <= Node.val <= 1000
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    before_half, fast = head, head
    while fast.next and fast.next.next:
        before_half = before_half.next
        fast = fast.next.next

    prev, cur = None, before_half.next
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    before_half.next = None

    left, right = head, prev
    while left and right:
        left_tmp = left.next
        right_tmp = right.next
        left.next = right
        right.next = left_tmp
        left = left_tmp
        right = right_tmp

    return head


def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def run_tests():
    test_cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        # 单节点
        ([1], [1]),
        # 两个节点
        ([1, 2], [1, 2]),
        # 三个节点
        ([1, 2, 3], [1, 3, 2]),
    ]
    for i, (vals, expected) in enumerate(test_cases):
        head = make_list(vals)
        reorderList(head)
        result = to_list(head)
        if result == expected:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected}, Got: {result}')


if __name__ == '__main__':
    run_tests()
