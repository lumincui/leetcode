"""
55. Jump Game - 跳跃游戏
难度: Medium | 类型: greedy
链接: https://leetcode.com/problems/jump-game/

题目描述:
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1:
输入: nums = [2,3,1,1,4]
输出: true
解释: 可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2:
输入: nums = [3,2,1,0,4]
输出: false
解释: 无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

约束:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""
from math import inf
from typing import List

def canJump(nums: List[int]) -> bool:
    dp = [False] * len(nums)
    dp[0] = True
    for i in range(len(nums)):
        if not dp[i]:
            continue
        for j in range(i+1,i+nums[i]+1):
            if j >= len(nums):
                break
            dp[j] = True

    return dp[-1]

def run_tests():
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
        ([2, 5, 0, 0], True),
        ([0, 2, 3], False),
    ]
    
    passed = 0
    for i, (nums, expected) in enumerate(test_cases):
        result = canJump(nums)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: nums={nums}, expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
