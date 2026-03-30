"""
236. Lowest Common Ancestor of a Binary Tree - 二叉树的最近公共祖先
难度: Medium | 类型: tree
链接: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

题目描述:
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3:
输入: root = [1,2], p = 1, q = 2
输出: 1

约束:
- 树中节点数目在范围 [2, 10^5] 内。
- -10^9 <= Node.val <= 10^9
- 所有 Node.val 互不相同 。
- p != q
- p 和 q 均存在于给定的二叉树中。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node):
        if not node:
            return None

        if node.val == p.val or node.val == q.val:
            return node

        left =  dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node
        return left or right
    return dfs(root)


# ===================== 测试工具 =====================
from collections import deque

def make_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

def find_node(root, val):
    if not root: return None
    if root.val == val: return root
    left = find_node(root.left, val)
    if left: return left
    return find_node(root.right, val)

def run_tests():
    test_cases = [
        ([3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3),
        ([3,5,1,6,2,0,8,None,None,7,4], 5, 4, 5),
        ([1,2], 1, 2, 1)
    ]
    
    passed = 0
    for i, (vals, p_val, q_val, expected) in enumerate(test_cases):
        root = make_tree(vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        
        result = lowestCommonAncestor(root, p, q)
        if result and result.val == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            got_val = result.val if result else None
            print(f"Test {i+1} FAIL: p={p_val}, q={q_val}, expected={expected}, got={got_val}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
