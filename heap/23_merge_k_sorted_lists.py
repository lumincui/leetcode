"""
23. Merge K Sorted Lists - 合并K个有序链表
难度: Medium | 类型: heap
链接: https://leetcode.com/problems/merge-k-sorted-lists/

题目描述:
    合并 K 个有序链表，返回合并后的有序链表。

示例:
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]

约束:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(vals):
    """从列表构建链表，返回头节点"""
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_list(head):
    """将链表转换为列表"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, chain in enumerate(lists):
        if chain:
            heapq.heappush(heap, (chain.val, i))

    root = ListNode(val=-1, next=None)
    prev = root
    while heap:
        val, i = heapq.heappop(heap)
        n = lists[i]
        prev.next = n
        prev = prev.next
        lists[i] = n.next

        if n.next:
            heapq.heappush(heap, (n.next.val, i))

    return root.next


def run_tests():
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6], "官方示例"),
        ([], [], "空链表列表"),
        ([[]], [], "单个空链表"),
        ([[1]], [1], "单个元素链表"),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6], "两个有序链表"),
        ([[-1, 0, 1], [2, 3, 4]], [-1, 0, 1, 2, 3, 4], "含负数"),
        ([[1, 1, 1], [1, 1, 1]], [1, 1, 1, 1, 1, 1], "重复元素多"),
    ]

    passed = 0
    for args, expected, desc in test_cases:
        lists = [make_list(l) for l in args]
        result = to_list(mergeKLists(lists))
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
