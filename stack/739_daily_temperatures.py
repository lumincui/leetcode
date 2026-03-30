"""
739. Daily Temperatures - 每日温度
难度: Medium | 类型: stack
链接: https://leetcode.com/problems/daily-temperatures/

题目描述:
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]

约束:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    waiting = []
    for i in range(len(temperatures)):
        while waiting:
            if temperatures[waiting[-1]] < temperatures[i]:
                answer[waiting[-1]] = i-waiting[-1]
                waiting.pop()
            else:
                break
        waiting.append(i)

    return answer


def run_tests():
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])
    ]
    
    passed = 0
    for i, (temps, expected) in enumerate(test_cases):
        # 传入副本以防修改原数组
        result = dailyTemperatures(temps[:])
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL:\n    temps={temps}\n    expected={expected}\n         got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
