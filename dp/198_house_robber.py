"""
198. House Robber - 打家劫舍
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/house-robber/

题目描述:
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内藏有现金，围成一条街道。
    如果两间相邻的房屋在同一晚上被偷，系统会自动报警。
    给定一个代表每间房现金金额的非负整数数组 nums，计算你在不触动警报的情况下，今晚能偷窃到的最高金额。

示例:
    输入: nums = [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房 (金额=1) 和 3 号房 (金额=3)，总计 4。

    输入: nums = [2,7,9,3,1]
    输出: 12
    解释: 偷窃 1 号房 (金额=2), 3 号房 (金额=9), 5 号房 (金额=1) = 12。

约束:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400
"""

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums)< 2:
        return max(nums)
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for k in range(2, len(nums)):
        dp[k] = max(nums[k] + dp[k-2], dp[k-1])

    return dp[len(nums)-1]


# ─────────────────────────── 测试框架 ───────────────────────────

def run_tests():
    test_cases = [
        ([1, 2, 3, 1], 4, "标准用例"),
        ([2, 7, 9, 3, 1], 12, "较长用例"),
        ([0], 0, "单零"),
        ([1], 1, "单元素"),
        ([2, 1, 1, 2], 4, "四元素"),
        ([1, 3, 1, 3, 100], 103, "含大数"),
        ([1, 2, 3, 4, 5], 9, "递增序列"),
        ([5, 1, 2, 10, 3, 2, 5], 17, "混合"),
        ([2, 1, 2, 7, 3, 1, 5], 13, "复杂混合"),
    ]

    passed = 0
    failed = 0

    for nums, expected, desc in test_cases:
        result = rob(nums)

        if result is None:
            print(f"FAIL [{desc}] nums={nums}: 返回 None")
            failed += 1
            continue

        if result != expected:
            print(f"FAIL [{desc}] nums={nums}: 期望 {expected}，实际 {result}")
            failed += 1
        else:
            print(f"PASS [{desc}] nums={nums} -> {result}")
            passed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败 / {passed + failed} 总计")


if __name__ == "__main__":
    run_tests()
