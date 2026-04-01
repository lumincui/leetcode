"""
78. Subsets - 子集
难度: Medium | 类型: backtracking
链接: https://leetcode.com/problems/subsets/

题目描述:
    给定一个不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    解集不能包含重复的子集，返回的结果可以按任意顺序排列。

示例:
    输入: nums = [1,2,3]
    输出: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

    输入: nums = [0]
    输出: [[], [0]]

约束:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - nums 中的所有元素互不相同
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[]]

    return [nums[:1] + ss for ss in subsets(nums[1:])] + subsets(nums[1:])


# ─────────────────────────── 测试框架 ───────────────────────────

def sorted_result(result):
    """将结果标准化排序，便于比较。"""
    return sorted([sorted(subset) for subset in result])


def run_tests():
    test_cases = [
        # (输入, 期望子集数量, 描述)
        ([1, 2, 3], 8, "标准三元素"),
        ([0], 2, "单元素0"),
        ([1], 2, "单元素1"),
        ([-1, 0, 1], 8, "含负数三元素"),
        ([1, 2], 4, "两元素"),
        ([1, 2, 3, 4], 16, "四元素"),
        ([-10, 10], 4, "极值两元素"),
    ]

    expected_full = {
        (1, 2, 3): [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        (0,): [[], [0]],
        (1,): [[], [1]],
        (1, 2): [[], [1], [2], [1, 2]],
    }

    passed = 0
    failed = 0

    for nums, expected_count, desc in test_cases:
        result = subsets(nums)

        if result is None:
            print(f"FAIL [{desc}] nums={nums}: 返回 None")
            failed += 1
            continue

        # 检查数量
        if len(result) != expected_count:
            print(f"FAIL [{desc}] nums={nums}: 期望 {expected_count} 个子集，实际 {len(result)} 个")
            failed += 1
            continue

        # 检查无重复
        normalized = [tuple(sorted(s)) for s in result]
        if len(normalized) != len(set(normalized)):
            print(f"FAIL [{desc}] nums={nums}: 结果含重复子集")
            failed += 1
            continue

        # 对特定用例检查内容
        key = tuple(sorted(nums))
        if key in expected_full:
            exp_sorted = sorted_result(expected_full[key])
            got_sorted = sorted_result(result)
            if exp_sorted != got_sorted:
                print(f"FAIL [{desc}] nums={nums}: 内容不匹配\n  期望: {exp_sorted}\n  实际: {got_sorted}")
                failed += 1
                continue

        print(f"PASS [{desc}] nums={nums} -> {len(result)} 个子集")
        passed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败 / {passed + failed} 总计")


if __name__ == "__main__":
    run_tests()
