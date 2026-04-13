"""
209. Minimum Size Subarray Sum - 长度最小的子数组
难度: Medium | 类型: sliding_window
链接: https://leetcode.com/problems/minimum-size-subarray-sum/

题目描述:
    给定一个含有 n 个正整数的数组和一个正整数 target。
    找出该数组中满足其和 ≥ target 的连续子数组的最小长度，返回其长度。如果不存在这样的子数组，返回 0。

示例:
    示例 1:
    输入: target = 7, nums = [2,3,1,2,4,3]
    输出: 2
    解释: 子数组 [4,3] 是该条件下的最小长度。

    示例 2:
    输入: target = 4, nums = [1,4,4]
    输出: 1

    示例 3:
    输入: target = 11, nums = [1,1,1,1,1,1,1,1]
    输出: 0

约束:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    min_length = float("inf")
    left, right = 0, 0
    window_sum = 0

    while right < len(nums):
        window_sum += nums[right]
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
        right += 1

    return 0 if min_length == float("inf") else int(min_length)


def run_tests():
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2, "官方示例1"),
        (4, [1, 4, 4], 1, "官方示例2"),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0, "官方示例3"),
        (15, [1, 2, 3, 4, 5], 5, "需要整个数组"),
        (3, [1, 1, 1], 3, "全1数组"),
        (5, [2, 2, 2, 2], 3, "永远达不到"),
        (1, [1], 1, "单元素刚好"),
        (1, [5], 1, "单元素超过"),
    ]

    passed = 0
    for target, nums, expected, desc in test_cases:
        result = min_sub_array_len(target, nums)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
