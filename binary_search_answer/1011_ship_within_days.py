"""
1011. Capacity To Ship Packages Within D Days
难度: Medium | 类型: binary_search_answer
链接: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

题目描述:
    传送带以 fixed_rate 每天运送包裹。
    给定一个包含包裹重量的数组 weights 和天数 days，在 days 天内运完所有包裹的最小运载能力是多少。

示例:
    weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    输出: 15 (每天运载能力15可以在5天内运完)

约束:
    1 <= weights.length <= 5 * 10^4
    1 <= weights[i] <= 500
"""

from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    left_rate, right_rate = max(weights), sum(weights)

    while left_rate < right_rate:
        mid_rate = (left_rate + right_rate) // 2

        d = 1
        package = 0
        for i, w in enumerate(weights):
            if package + w > mid_rate:
                d += 1
                package = 0

            package += w

        if d <= days:
            right_rate = mid_rate
        else:
            left_rate = mid_rate

    return right_rate


def can_ship(capacity: int, weights: List[int], days: int) -> bool:
    """检查给定运载能力是否能在days天内运完"""
    current_day = 1
    current_weight = 0
    for w in weights:
        if current_weight + w > capacity:
            current_day += 1
            current_weight = w
            if current_day > days:
                return False
        else:
            current_weight += w
    return True


def run_tests():
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15, "官方示例"),
        ([1, 2, 3, 4, 5, 6], 3, 6, "三天运完"),
        ([1, 2, 3, 4, 5], 5, 5, "五天每天一个"),
        ([3, 2, 2, 1], 2, 3, "两天运完"),
    ]

    passed = 0
    for weights, days, expected, desc in test_cases:
        result = shipWithinDays(weights, days)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
