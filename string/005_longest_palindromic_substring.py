'''
5. Longest Palindromic Substring
难度: Medium | 类型: string
链接: https://leetcode.com/problems/longest-palindromic-substring/

题目描述:
    给你一个字符串 s，找出 s 中最长的回文子串。

示例:
    输入: s = "babad"    →  "bab" 或 "aba"
    输入: s = "cbbd"     →  "bb"

约束:
    1 <= s.length <= 1000
    s 仅由数字和英文字母组成
'''

def longestPalindrome(s: str) -> str:
    longest = ''
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left = left - 1
            right = right + 1


        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left = left - 1
            right = right + 1
    return longest


def run_tests():
    test_cases = [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
    ]
    for i, (s, expected) in enumerate(test_cases):
        res = longestPalindrome(s)
        ok = res in [expected, expected[::-1]]
        if ok:
            print(f"PASS: Case {i+1} | s={s} → {res}")
        else:
            print(f"FAIL: Case {i+1} | s={s} | Expected: {expected}, Got: {res}")

if __name__ == '__main__':
    run_tests()
