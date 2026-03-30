'''
994. Rotting Oranges
难度: Medium | 类型: 图 / 多源 BFS
链接: https://leetcode.com/problems/rotting-oranges/

题目描述:
    给你一个 m x n 的网格 grid，每个单元格有三种值：
      0：空单元格
      1：新鲜橘子
      2：腐烂橘子
    每分钟，所有腐烂橘子的上下左右相邻新鲜橘子都会变腐烂。
    返回直到没有新鲜橘子为止所需的最少分钟数。
    如果不可能让所有橘子腐烂，返回 -1。

示例:
    Input: [[2,1,1],[1,1,0],[0,1,1]]  -> Output: 4
    Input: [[2,1,1],[0,1,1],[1,0,0]]  -> Output: -1
    Input: [[0,2]]                    -> Output: 0

约束:
    - 1 <= m, n <= 10
    - grid[i][j] in {0, 1, 2}
'''

from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    queue = []
    next_queue = []
    minutes = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                queue.append((i, j))

    while queue or next_queue:
        if not queue:
            minutes += 1
            queue = next_queue
            next_queue = []

        while queue:
            (x, y) = queue.pop()
            if 0 <= x-1 < len(grid) and grid[x-1][y] == 1:
                next_queue.append((x-1, y))
                grid[x-1][y] = 2
            if 0 <= x+1 < len(grid) and grid[x+1][y] == 1:
                next_queue.append((x+1, y))
                grid[x+1][y] = 2
            if 0 <= y-1 < len(grid[x]) and grid[x][y-1] == 1:
                next_queue.append((x, y-1))
                grid[x][y-1] = 2
            if 0 <= y+1 < len(grid[x]) and grid[x][y+1] == 1:
                next_queue.append((x, y+1))
                grid[x][y+1] = 2

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return minutes


def run_tests():
    test_cases = [
        ([[2,1,1],[1,1,0],[0,1,1]],         4),
        ([[2,1,1],[0,1,1],[1,0,0]],         -1),   # 孤立新鲜橘子
        ([[0,2]],                            0),   # 无新鲜橘子
        ([[1]],                             -1),   # 只有新鲜，无腐烂
        ([[2]],                              0),   # 只有腐烂
        ([[2,1],[1,1]],                      2),   # 2x2
        ([[0]],                              0),   # 全空
    ]
    all_pass = True
    for i, (grid, expected) in enumerate(test_cases):
        # 深拷贝避免原地修改影响后续用例
        import copy
        result = orangesRotting(copy.deepcopy(grid))
        if result == expected:
            print(f"PASS: Case {i+1}  grid={grid} -> {result}")
        else:
            print(f"FAIL: Case {i+1}  grid={grid} | Expected: {expected}, Got: {result}")
            all_pass = False
    print()
    print("All tests passed!" if all_pass else "Some tests FAILED.")


if __name__ == '__main__':
    run_tests()
