"""
1143. Longest Common Subsequence - 最长公共子序列
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/longest-common-subsequence/

题目描述:
    给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
    如果不存在公共子序列，返回 0。

    一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

示例:
    输入: text1 = "abcde", text2 = "ace"
    输出: 3
    解释: 最长公共子序列是 "ace"，其长度为 3。

    输入: text1 = "abc", text2 = "abc"
    输出: 3
    解释: 最长公共子序列是 "abc"，其长度为 3。

    输入: text1 = "abc", text2 = "def"
    输出: 0
    解释: 两个字符串没有公共子序列。

约束:
    1 <= text1.length, text2.length <= 1000
    text1 和 text2 仅由小写英文字符组成。
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = [[0 for _ in text2] for _ in text1]

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = (dp[i-1][j-1] if i != 0 and j != 0 else 0) + 1
            else:
                dp[i][j] = max(dp[i-1][j] if i != 0 else 0, dp[i][j-1] if j != 0 else 0)

    return dp[-1][-1]

def run_tests() -> None:
    test_cases = [
        # 题目示例
        {"text1": "abcde", "text2": "ace", "expected": 3},
        {"text1": "abc", "text2": "abc", "expected": 3},
        {"text1": "abc", "text2": "def", "expected": 0},
        # 边界和常见场景
        {"text1": "a", "text2": "a", "expected": 1},
        {"text1": "a", "text2": "b", "expected": 0},
        {"text1": "bl", "text2": "ybyl", "expected": 2},
        {"text1": "pmjghexybyrgzczy", "text2": "hafcdqbgncrcbihkd", "expected": 4},
    ]

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        got = longest_common_subsequence(tc["text1"], tc["text2"])
        ok = got == tc["expected"]
        if ok:
            passed += 1
            print(f"[PASS] case #{i}: got={got}")
        else:
            print(
                f"[FAIL] case #{i}: text1={tc['text1']!r}, text2={tc['text2']!r}, "
                f"expected={tc['expected']}, got={got}"
            )

    print(f"\nResult: {passed}/{total} passed")


if __name__ == "__main__":
    run_tests()
