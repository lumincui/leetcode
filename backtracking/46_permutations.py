"""
46. Permutations - 全排列
难度: Medium | 类型: backtracking
链接: https://leetcode.com/problems/permutations/

题目描述:
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1:
输入: nums = [1,2,3]
输出: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2:
输入: nums = [0,1]
输出: [[0,1],[1,0]]

示例 3:
输入: nums = [1]
输出: [[1]]

约束:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- nums 中的所有整数 互不相同
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]

    result = []
    for i in range(len(nums)):
        cur = nums[i]
        others = nums[:i] + nums[i+1:]

        next = permute(others)
        for i in range(len(next)):
            next[i] = [cur] + next[i]

        result += next

    return result




def run_tests():
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ]
    
    passed = 0
    for i, (nums, expected) in enumerate(test_cases):
        result = permute(nums)
        if result is None:
            result = []
            
        # 结果的顺序不重要，所以将外层列表排序后再比较
        sorted_result = sorted(result)
        sorted_expected = sorted(expected)
        
        if sorted_result == sorted_expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: nums={nums}\n    expected={sorted_expected}\n         got={sorted_result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
