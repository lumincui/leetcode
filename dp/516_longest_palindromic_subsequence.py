'''
516. Longest Palindromic Subsequence
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/longest-palindromic-subsequence/

题目描述:
    给你一个字符串 s，找出其中最长的回文子序列的长度。

示例:
    输入: s = "bbbab"  →  4 ("bbbb")
    输入: s = "cbbd"   →  2 ("bb")

约束:
    1 <= s.length <= 1000
'''

def longestPalindromeSubseq(s: str) -> int:
    dp = [[0] * len(s) for _ in s]
    for i in range(len(s)):
        dp[i][i] = 1

    for L in range(2, len(s)+1):
        for i in range(len(s)-L+1):
            j = i + L - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][len(s)-1]

def run_tests():
    test_cases = [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("abcde", 1),
    ]
    for i, (s, expected) in enumerate(test_cases):
        res = longestPalindromeSubseq(s)
        if res == expected:
            print(f"PASS: Case {i+1}")
        else:
            print(f"FAIL: Case {i+1} | Expected: {expected}, Got: {res}")

if __name__ == '__main__':
    run_tests()
