"""
56. Merge Intervals - 合并区间
难度: Medium | 类型: intervals
链接: https://leetcode.com/problems/merge-intervals/

题目描述:
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间.

约束:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    for intv in intervals:
        if len(result) == 0:
            result.append(intv)
            continue

        last = result[-1]
        if intv[0] > last[1]:
            result.append(intv)
            continue

        if intv[0] <= last[1]:
            if intv[1] <= last[1]:
                continue
            else:
                result[-1][1] = intv[1]


    return result


def run_tests():
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[1,4],[0,0]], [[0,0],[1,4]]),
    ]
    
    passed = 0
    for i, (intervals, expected) in enumerate(test_cases):
        # 复制输入以避免原地修改影响测试
        intervals_copy = [row[:] for row in intervals]
        result = merge(intervals_copy)
        
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: intervals={intervals}\n    expected={expected}\n         got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
