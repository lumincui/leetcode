"""
91. Decode Ways
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/decode-ways/

题目描述:
    一条包含 'A'-'Z' 的消息需要解码成数字。每条字母映射到数字 1-26。
    给定只含数字的字符串 s，返回解码方式总数。

示例:
    Input: s = "12"
    Output: 2
    解释: "AB" (1 2) 或 "L" (12)

    Input: s = "226"
    Output: 3
    解释: "BZ" (2 26), "BBF" (2 2 6), 或 "VF" (22 6)

    Input: s = "06"
    Output: 0
    解释: "06" 不能被解码（'6' 前缀 '0' 无效）

约束:
    1 <= s.length <= 100
    s 只含数字，首字符不为 '0'
"""

from typing import List


def num_decodings(s: str) -> int:
    if not s:
        return 0

    dp = [0] * len(s)

    for i in range(len(s)):
        if s[i] != '0':
            dp[i] += dp[i-1] if i-1>= 0 else 1
        if i-1>=0 and 10<= int(s[i-1:i+1]) <= 26:
            dp[i] += dp[i-2] if i-2>= 0 else 1

    return dp[-1]

def run_tests():
    test_cases = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("10", 1),
        ("101", 1),
        ("11111111111111111111", 10946),
        ("27", 1),
        ("110", 1),
        ("1001", 0),
        ("", 0),
    ]

    for i, (s, expected) in enumerate(test_cases):
        try:
            result = num_decodings(s)
            if result == expected:
                print(f"PASS: case {i+1} - num_decodings({s!r}) = {result}")
            else:
                print(f"FAIL: case {i+1} - num_decodings({s!r}) = {result}, expected {expected}")
        except Exception as e:
            print(f"ERROR: case {i+1} - num_decodings({s!r}) raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    run_tests()
