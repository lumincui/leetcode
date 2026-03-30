"""
322. Coin Change - 零钱兑换
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/coin-change/

题目描述:
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

示例 3:
输入: coins = [1], amount = 0
输出: 0

约束:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""
import math
from math import inf
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for am in range(1, amount+1):
        for c in coins:
            if c > am:
                continue

            dp[am] = min(dp[am], dp[am-c] + 1)

    return dp[amount] if dp[amount] != math.inf else -1



def run_tests():
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([186, 419, 83, 408], 6249, 20),
        ([1, 2, 5], 100, 20),
        ([3, 7, 405, 436], 8839, 25),
    ]
    
    passed = 0
    for i, (coins, amount, expected) in enumerate(test_cases):
        result = coinChange(coins, amount)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: coins={coins}, amount={amount}, expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
