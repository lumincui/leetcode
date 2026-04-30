"""
17. Letter Combinations of a Phone Number - 电话号码字母组合
难度: Medium | 类型: backtracking
链接: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

题目描述:
    给定一个仅包含数字 2-9 的字符串，返回它能表示的所有字母组合。
    数字到字母的映射如下:
    2 -> abc
    3 -> def
    4 -> ghi
    5 -> jkl
    6 -> mno
    7 -> pqrs
    8 -> tuv
    9 -> wxyz

示例:
    输入: "23"
    输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

约束:
    - 0 <= digits.length <= 4
    - digits 仅包含字符 '2'-'9'
"""

from typing import List

from numpy.ma.core import diag

mapping = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return [""]

    digit, remain = digits[0], digits[1:]

    subs = letter_combinations(remain)
    return [alpha + sub for alpha in mapping[int(digit)] for sub in subs]


def run_tests():
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "官方示例 23"),
        ("", [""], "空字符串"),
        ("2", ["a", "b", "c"], "单个数字"),
        ("7", ["p", "q", "r", "s"], "7对应4个字母"),
        (
            "79",
            [
                "pw",
                "px",
                "py",
                "pz",
                "qw",
                "qx",
                "qy",
                "qz",
                "rw",
                "rx",
                "ry",
                "rz",
                "sw",
                "sx",
                "sy",
                "sz",
            ],
            "7+9组合",
        ),
    ]

    passed = 0
    for args, expected, desc in test_cases:
        result = letter_combinations(args)
        if result is None:
            print(f"FAIL: {desc} - Function returned None")
            continue
        result_set = set(result)
        expected_set = set(expected)
        if result_set == expected_set:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
