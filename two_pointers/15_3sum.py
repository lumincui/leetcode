"""
15. 3Sum - 三数之和
难度: Medium | 类型: two_pointers
链接: https://leetcode.com/problems/3sum/

题目描述:
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1:
输入: nums = [-1,0,1,2,-1,-4]
输出: [[-1,-1,2],[-1,0,1]]
解释:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。

示例 2:
输入: nums = [0,1,1]
输出: []
解释: 唯一可能的三元组和不为 0 。

示例 3:
输入: nums = [0,0,0]
输出: [[0,0,0]]
解释: 唯一可能的三元组和为 0 。

约束:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i + 1, len(nums)-1
        while j != k and j < len(nums):
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                hit_j, hit_k = nums[j], nums[k]
                while  j != k and nums[j] == hit_j:
                    j = j + 1
                while j != k and nums[k] == hit_k:
                    k = k - 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k = k - 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j = j + 1
    return result



def run_tests():
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]
    
    passed = 0
    for i, (nums, expected) in enumerate(test_cases):
        # Sort inner lists to compare sets of lists easily
        result = threeSum(nums)
        if result is None:
            result = []
            
        sorted_result = sorted([sorted(x) for x in result])
        sorted_expected = sorted([sorted(x) for x in expected])
        
        if sorted_result == sorted_expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: input={nums}\n    expected={sorted_expected}\n         got={sorted_result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
