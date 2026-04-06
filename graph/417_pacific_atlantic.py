"""
417. Pacific Atlantic Water Flow - 太平洋大西洋水流
难度: Medium | 类型: graph
链接: https://leetcode.com/problems/pacific-atlantic-water-flow/

题目描述:
    给定一个 m x n 的非负整数矩阵 heights，表示陆地区域的高度。
    太平洋位于矩阵的左边和上边，大西洋位于矩阵的右边和下边。
    如果一个单元格能够同时流向太平洋和大西洋，则将其加入结果列表。
    水只能从高处流向低处或相同高度的位置。

示例:
    示例1:
    heights = [
        [1,2,2,3,1],
        [3,8,7,7,2],
        [5,9,10,9,3],
        [2,2,1,1,2]
    ]
    输出: [[0,3],[1,3],[2,1],[3,0],[3,1]]

    示例2:
    heights = [[1]]
    输出: [[0,0]]

约束:
    1 <= m, n <= 200
    1 <= heights[i][j] <= 10^5
"""

from typing import List

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    def accessible(matrix: List[List[int]]):
        visited = set()
        def dfs(x, y):
            if (x, y) in visited:
                return

            visited.add((x, y))

            if 0 <= x-1 < len(matrix) and matrix[x-1][y] > matrix[x][y]:
                dfs(x-1, y)
            if 0 <= x+1 < len(matrix) and matrix[x+1][y] > matrix[x][y]:
                dfs(x+1, y)
            if 0 <= y-1 < len(matrix[0]) and matrix[x][y-1] > matrix[x][y]:
                dfs(x, y-1)
            if 0 <= y+1 < len(matrix[0]) and matrix[x][y+1] > matrix[x][y]:
                dfs(x, y+1)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    dfs(i, j)

        return visited


    pacific = [[0] * (len(heights[0]) + 1)] + [[0] + [cel for cel in row] for row in heights]
    atlantic = [[cel for cel in row] + [0] for row in heights] + [[0] * (len(heights[0]) + 1)]

    pacific = set((x-1,y-1) for x,y in accessible(pacific) if x-1>0 and y-1 > 0)
    atlantic = set((x+1,y+1) for x,y in accessible(atlantic) if x+1<len(heights) and y+1<len(heights[0]))

    return pacific.intersection(atlantic)

def run_tests():
    test_cases = [
        (
            [
                [1, 2, 2, 3, 1],
                [3, 8, 7, 7, 2],
                [5, 9, 10, 9, 3],
                [2, 2, 1, 1, 2]
            ],
            [[0, 3], [1, 3], [2, 1], [3, 0], [3, 1]],
            "官方示例"
        ),
        (
            [[1]],
            [[0, 0]],
            "单单元格"
        ),
        (
            [
                [1, 2, 3],
                [8, 9, 4],
                [7, 6, 5]
            ],
            [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]],
            "所有单元格都可到达至少一个海洋"
        ),
        (
            [
                [2, 1],
                [1, 2]
            ],
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            "所有单元格都同时流向两边"
        ),
        (
            [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]
            ],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
            "高度相同矩阵"
        ),
        (
            [
                [1, 3, 4],
                [3, 2, 5]
            ],
            [[0, 2], [1, 0], [1, 1], [1, 2]],
            "边缘仅部分可达"
        ),
    ]
    
    passed = 0
    for heights, expected, desc in test_cases:
        result = pacific_atlantic(heights)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        if result_sorted == expected_sorted:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected_sorted}, got {result_sorted}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
