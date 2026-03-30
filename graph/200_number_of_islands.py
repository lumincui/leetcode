"""
200. Number of Islands - 岛屿数量
难度: Medium | 类型: graph
链接: https://leetcode.com/problems/number-of-islands/

题目描述:
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出: 1

示例 2:
输入: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出: 3

约束:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] 的值为 '0' 或 '1'
"""

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == '0':
            return

        grid[i][j] = '0'
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count


def run_tests():
    test_cases = [
        ([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1),
        ([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3),
        ([
            ["0","0","0"],
            ["0","0","0"]
        ], 0),
        ([
            ["1","0","1"],
            ["0","1","0"],
            ["1","0","1"]
        ], 5),
        ([
            ["1"]
        ], 1)
    ]
    
    passed = 0
    for i, (grid, expected) in enumerate(test_cases):
        # Create a deep copy of the grid since the function might modify it
        grid_copy = [row[:] for row in grid]
        result = numIslands(grid_copy)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
