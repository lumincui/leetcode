'''
39. Combination Sum
难度: Medium | 类型: backtracking
链接: https://leetcode.com/problems/combination-sum/

题目描述:
    给定一个无重复元素的整数数组 candidates 和一个目标整数 target，
    找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的同一个数字可以无限制重复被选取。
    结果中的组合可以以任意顺序返回，但每个组合内的数字必须按非递减顺序排列。

示例:
    输入: candidates = [2,3,6,7], target = 7
    输出: [[2,2,3],[7]]

    输入: candidates = [2,3,5], target = 8
    输出: [[2,2,2,2],[2,3,3],[3,5]]

约束:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - candidates 中所有元素互不相同
    - 1 <= target <= 40
'''

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    if not candidates:
        return result

    first = candidates[0]
    if first == target:
        result.append([first])

    if first < target:
        subs = combinationSum(candidates, target-first)
        for sub in subs:
            result.append([first, *sub])

    subs = combinationSum(candidates[1:], target)
    result += subs
    return result


def run_tests():
    test_cases = [
        (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
        (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        # 单元素恰好整除
        (([3], 9), [[3, 3, 3]]),
        # 无解
        (([5], 3), []),
        # 单元素等于target
        (([7], 7), [[7]]),
    ]
    for i, ((candidates, target), expected) in enumerate(test_cases):
        result = combinationSum(candidates, target)
        result_sorted = sorted([sorted(c) for c in result])
        expected_sorted = sorted([sorted(c) for c in expected])
        if result_sorted == expected_sorted:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected_sorted}, Got: {result_sorted}')


if __name__ == '__main__':
    run_tests()
