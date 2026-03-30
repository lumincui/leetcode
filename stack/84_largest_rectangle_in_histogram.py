'''
84. Largest Rectangle in Histogram
难度: Hard | 类型: 单调栈
链接: https://leetcode.com/problems/largest-rectangle-in-histogram/

题目描述:
    给定一个整数数组 heights，表示柱状图中每根柱子的高度，每根柱子宽度为 1。
    返回柱状图中能勾勒出的最大矩形面积。

示例:
    输入: heights = [2,1,5,6,2,3]  →  输出: 10
    输入: heights = [2,4]           →  输出: 4

约束:
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4
'''


def largestRectangleArea(heights: list) -> int:
    stack = []
    max_area = 0
    heights.append(0)

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


def run_tests():
    test_cases = [
        (([2, 1, 5, 6, 2, 3],), 10),
        (([2, 4],), 4),
        (([1],), 1),
        (([1, 1],), 2),
        (([0],), 0),
        (([6, 7, 5, 2, 4, 5, 9, 3],), 16),
    ]
    for i, (inputs, expected) in enumerate(test_cases):
        result = largestRectangleArea(*inputs)
        if result == expected:
            print(f"PASS: Case {i+1}")
        else:
            print(f"FAIL: Case {i+1} | Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()
