"""
142. Linked List Cycle II - 环形链表 II
难度: Medium | 类型: fast_slow_pointers
链接: https://leetcode.com/problems/linked-list-cycle-ii/

题目描述:
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

示例 1:
输入: head = [3,2,0,-4], pos = 1
输出: 返回索引为 1 的链表节点
解释: 链表中有一个环，其尾部连接到第二个节点。

示例 2:
输入: head = [1,2], pos = 0
输出: 返回索引为 0 的链表节点
解释: 链表中有一个环，其尾部连接到第一个节点。

示例 3:
输入: head = [1], pos = -1
输出: 返回 null
解释: 链表中没有环。

约束:
- 链表中节点的数目范围在范围 [0, 10^4] 内
- -10^5 <= Node.val <= 10^5
- pos 的值为 -1 或者链表中的一个有效索引
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# ===================== 测试工具 =====================
def make_cycle_list(vals, pos):
    if not vals:
        return None, None
    
    nodes = [ListNode(val) for val in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        
    if pos != -1:
        nodes[-1].next = nodes[pos]
        
    return nodes[0], (nodes[pos] if pos != -1 else None)

def run_tests():
    test_cases = [
        # 原有测试用例
        ([3, 2, 0, -4], 1),          # 标准4节点环
        ([1, 2], 0),                  # 2节点自环
        ([1], -1),                    # 单节点无环
        ([], -1),                     # 空链表

        # 补充边界用例
        ([1], 0),                     # 单节点自环
        ([1, 2, 3], 0),               # 全环，环入口为首节点
        ([1, 2, 3, 4], 3),            # 环入口为尾节点
        ([1, 2, 3, 4, 5], -1),        # 长链表无环
        ([1, 2, 3, 4, 5], 2),         # 环在中间位置
        ([1, 2], -1),                 # 2节点无环
        ([1, 2, 3], 0),               # 3节点环回首个
        ([-1, -2, -3], 1),            # 负数节点值
        ([100, 200, 300], 0),         # 大数值节点
        ([1, 2, 3, 4, 5], 3),         # 环入口为倒数第二个
    ]
    
    passed = 0
    for i, (vals, pos) in enumerate(test_cases):
        head, expected_node = make_cycle_list(vals, pos)
        result = detectCycle(head)
        
        if result is expected_node:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            exp_val = expected_node.val if expected_node else None
            res_val = result.val if result else None
            print(f"Test {i+1} FAIL: expected node with val={exp_val}, got node with val={res_val}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
