"""
139. Word Break - 单词拆分
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/word-break/

题目描述:
    给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
    判断 s 是否可以被空格分割成若干个在 wordDict 中出现的单词。
    单词可以重复使用。

示例:
    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true

    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true

    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

约束:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s 和 wordDict[i] 仅由小写英文字母组成
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[0] = True
    word_dict = set(word_dict)

    for j in range(1, len(s)+1):
        for i in range(j):
            dp[j] = dp[j] or s[i:j] in word_dict and dp[i]

    return dp[-1]

def run_tests():
    test_cases = [
        (("leetcode", ["leet", "code"]), True, "官方示例1"),
        (("applepenapple", ["apple", "pen"]), True, "官方示例2"),
        (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False, "官方示例3"),
        (("", ["a"]), True, "空字符串"),
        (("a", ["a"]), True, "单字符能匹配"),
        (("a", ["b"]), False, "单字符不能匹配"),
        (("aaaaaaa", ["aaaa", "aaa"]), True, "重叠分割"),
        (("bbb", ["b", "bb"]), True, "最短单词优先"),
        (("abcd", ["a", "bc", "d"]), True, "多种分割方式"),
        (("abcd", ["ab", "cd"]), True, "两词分割"),
    ]
    
    passed = 0
    for args, expected, desc in test_cases:
        result = word_break(*args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()