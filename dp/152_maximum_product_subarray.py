"""
152. Maximum Product Subarray - 乘积最大子数组
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/maximum-product-subarray/

题目描述:
    给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（子数组最少包含一个元素），
    并返回其乘积。

示例:
    示例 1:
    输入: nums = [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 的乘积最大，为 6

    示例 2:
    输入: nums = [-2,0,-1]
    输出: 0
    解释: 结果不能是 1，因为子数组乘积最大为 0

约束:
    - 1 <= nums.length <= 20
    - -10 <= nums[i] <= 10
    - 题目保证答案是一个 32 位整数
"""
from math import inf
from typing import List


def maxProduct(nums: List[int]) -> int:
    dp = [[-inf] * len(nums) for _ in nums]
    max_value = -inf

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            dp[i][j] = nums[j] * dp[i][j-1] if i != j else nums[i]
            max_value = max(max_value, dp[i][j])

    return max_value


def run_tests():
    test_cases = [
        ([2, 3, -2, 4], 6, "官方示例1"),
        ([-2, 0, -1], 0, "官方示例2"),
        ([-2, 3, -4], 24, "两个负数乘积最大"),
        ([2, -5, -2, -4, 3], 24, "复杂负数组合"),
        ([-1, -1], 1, "全负数"),
        ([1, 2, 3, 4, 5], 120, "全正数"),
        ([0, 2], 2, "含零"),
        ([-2], -2, "单负数"),
        ([0, -1], 0, "零和负数"),
        ([2, -1, 1, -1], 2, "交替正负"),
    ]

    passed = 0
    for nums, expected, desc in test_cases:
        result = maxProduct(nums)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
