"""
42. Trapping Rain Water - 接雨水
难度: Hard | 类型: Two Pointers / Stack / DP
链接: https://leetcode.com/problems/trapping-rain-water/

题目描述:
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算下雨之后能接多少雨水。

示例:
    输入: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

    输入: height = [4,2,0,3,2,5]
    输出: 9

约束:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""

from typing import List


def trap(height: List[int]) -> int:
    left, right = 0, len(height)-1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] > height[right]:
            right_max = max(height[right], right_max)
            water += right_max - height[right]
            right -= 1
        else:
            left_max = max(height[left], left_max)
            water += left_max - height[left]
            left += 1

    return water


def run_tests():
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, "官方示例1"),
        ([4, 2, 0, 3, 2, 5], 9, "官方示例2"),
        ([0], 0, "单个柱子无法接水"),
        ([1, 2, 3, 4, 5], 0, "严格递增无法接水"),
        ([5, 4, 3, 2, 1], 0, "严格递减无法接水"),
        ([3, 0, 3], 3, "简单凹槽"),
        ([5, 0, 0, 0, 5], 15, "宽凹槽"),
        ([2, 0, 2, 0, 2], 4, "多个等高边界凹槽"),
        ([4, 2, 3], 1, "右边界较低但仍可接水"),
        ([0, 2, 0, 2, 0], 2, "边缘为0不影响中间接水"),
    ]

    passed = 0
    for height, expected, desc in test_cases:
        result = trap(height)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
