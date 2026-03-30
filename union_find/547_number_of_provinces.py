"""
547. Number of Provinces - 省份数量
难度: Medium | 类型: union_find
链接: https://leetcode.com/problems/number-of-provinces/

题目描述:
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

示例 1:
输入: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出: 2

示例 2:
输入: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出: 3

约束:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] 为 1 或 0
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
"""

from typing import List

def findCircleNum(isConnected: List[List[int]]) -> int:
    parent = list(range(len(isConnected)))

    def union(a, b):
        parent[find(a)] = find(b)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if isConnected[i][j]:
                union(i, j)

    return len(set(find(i) for i in range(len(isConnected))))


def run_tests():
    test_cases = [
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
        ([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]], 1),
        ([[1]], 1),
    ]
    
    passed = 0
    for i, (isConnected, expected) in enumerate(test_cases):
        result = findCircleNum(isConnected)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
