"""
213. House Robber II - 打家劫舍 II
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/house-robber-ii/

题目描述:
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房都藏有现金，
    这些房屋形成一个圆形。相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被闯入，系统会自动报警。
    给定一个代表每间房存款金额的非负整数数组，计算你在不触动警报的情况下，
    今晚能够偷窃到的最高金额。

示例:
    示例 1:
    输入: nums = [2,3,2]
    输出: 3
    解释: 你不能先偷窃房屋 1（金额 = 3），然后偷窃房屋 3（金额 = 2），因为它们是相邻的。

    示例 2:
    输入: nums = [1,2,3,1]
    输出: 4
    解释: 你可以偷窃房屋 1（金额 = 1）和房屋 3（金额 = 3），偷窃总金额 = 1 + 3 = 4

    示例 3:
    输入: nums = [1,2,3]
    输出: 3

约束:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000
"""

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)

    def rob_line(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]

    return max(
        rob_line(nums[1:]),
        rob_line(nums[:-1]),
    )


def run_tests():
    test_cases = [
        ([2, 3, 2], 3, "官方示例1 - 环形数组"),
        ([1, 2, 3, 1], 4, "官方示例2 - 1和3不相邻"),
        ([1, 2, 3], 3, "官方示例3 - 首尾不能同时偷"),
        ([1], 1, "单房屋"),
        ([2], 2, "单房屋2"),
        ([1, 2], 2, "两房屋取较大"),
        ([2, 1, 2], 2, "中间房屋金额最大"),
        ([0], 0, "零金额"),
        ([0, 0], 0, "两零房屋"),
        ([1, 3, 1, 3, 100], 103, "复杂环形"),
    ]

    passed = 0
    for nums, expected, desc in test_cases:
        result = rob(nums)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
