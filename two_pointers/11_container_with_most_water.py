"""
11. Container With Most Water - 盛最多水的容器
难度: Medium | 类型: two_pointers
链接: https://leetcode.com/problems/container-with-most-water/

题目描述:
    给定一个长度为 n 的整数数组 height，有 n 条垂线。
    第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。
    找出其中的两条线，使得它们与 x 轴共同构成的容器能够容纳最多的水。

示例:
    输入: height = [1,8,6,2,5,4,8,3,7]
    输出: 49
    解释: 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。
    在此情况下，容器能够容纳水（表示为蓝色部分）的最大面积为 49。

    输入: height = [1,1]
    输出: 1

约束:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""

from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    biggest = 0

    while right > left:
        biggest = max(biggest, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

    return biggest


def run_tests():
    test_cases = [
        (([1,8,6,2,5,4,8,3,7],), 49, "官方示例1"),
        (([1,1],), 1, "官方示例2"),
        (([4,3,2,1,4],), 16, "对称数组"),
        (([1,2,1],), 2, "三元素"),
        (([1,2],), 1, "两元素"),
        (([2,3,10,5,2,8],), 24, "随机数组"),
        (([1,8,6,2,5,4,8,25,7],), 49, "大面积在中间"),
    ]
    
    passed = 0
    for args, expected, desc in test_cases:
        result = max_area(*args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()