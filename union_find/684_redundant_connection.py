"""
684. Redundant Connection - 冗余连接
难度: Medium | 类型: union_find
链接: https://leetcode.com/problems/redundant-connection/

题目描述:
    树可以看成是一个连通且无环的无向图。
    给定一个有 n 个节点（节点值 1 到 n）的图，这个图开始是一棵树，
    后来额外添加了一条边。添加的边连接两个不同的顶点，且不属于原树中已存在的边。
    图的信息由长度为 n 的二维数组 edges 表示，其中 edges[i] = [ai, bi]
    表示图中 ai 和 bi 之间有一条边。

    请找出一条可以删去的边，使得剩余图是一个有 n 个节点的树。
    如果有多个答案，返回在输入中最后出现的那条边。

示例:
    输入: edges = [[1,2],[1,3],[2,3]]
    输出: [2,3]

    输入: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    输出: [1,4]

约束:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    edges 中没有重复边
    给定图是连通的
"""

from typing import List, Tuple


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    # TODO: 在这里实现你的解法
    raise NotImplementedError("TODO: implement find_redundant_connection")


def run_tests() -> None:
    test_cases: List[Tuple[List[List[int]], List[int]]] = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
        ([[1, 2], [2, 3], [3, 1]], [3, 1]),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [2, 5]], [2, 5]),
        ([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]], [1, 3]),
    ]

    passed = 0
    total = len(test_cases)

    print("Running tests for 684. Redundant Connection")
    print("-" * 60)

    for i, (edges, expected) in enumerate(test_cases, start=1):
        try:
            actual = find_redundant_connection(edges)
            if actual == expected:
                passed += 1
                print(f"[PASS] Case {i}: edges={edges} -> {actual}")
            else:
                print(
                    f"[FAIL] Case {i}: edges={edges} -> expected {expected}, got {actual}"
                )
        except Exception as exc:
            print(f"[ERROR] Case {i}: edges={edges} -> {type(exc).__name__}: {exc}")

    print("-" * 60)
    print(f"Passed {passed}/{total} cases")


if __name__ == "__main__":
    run_tests()
