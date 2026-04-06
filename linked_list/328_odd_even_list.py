"""
328. Odd Even Linked List - 奇偶链表
难度: Medium | 类型: linked_list
链接: https://leetcode.com/problems/odd-even-linked-list/

题目描述:
    给定一个单链表，将所有索引为奇数的节点组合在一起，
    然后将索引为偶数的节点组合在一起，返回重排后的链表。
    请注意，这里是基于节点索引的奇偶性，而非节点值的奇偶。

示例:
    示例1:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL

    示例2:
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL

约束:
    链表长度范围 [1, 10^4]
    0 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    even, odd = head, head.next
    odd_head = head.next
    cur = odd.next
    order = 1

    while cur:
        if order%2 == 1:
            even.next = cur
            even = even.next
        else:
            odd.next = cur
            odd = odd.next

        cur = cur.next
        order += 1

    even.next = odd_head
    odd.next = None
    return head


def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4], "官方示例1"),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4], "官方示例2"),
        ([1], [1], "单节点"),
        ([1, 2], [1, 2], "两节点"),
        ([1, 2, 3], [1, 3, 2], "三节点"),
        ([1, 2, 3, 4], [1, 3, 2, 4], "四节点"),
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6], "六节点"),
    ]
    
    passed = 0
    for input_vals, expected, desc in test_cases:
        head = make_list(input_vals)
        result = odd_even_list(head)
        result_list = to_list(result)
        if result_list == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result_list}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
