"""
22. Generate Parentheses - 括号生成
难度: Medium | 类型: backtracking
链接: https://leetcode.com/problems/generate-parentheses/

题目描述:
    给定 n 对括号，编写一个函数来生成所有可能的、格式正确的括号组合。

示例:
    输入: n = 3
    输出: ["((()))","(()())","(())()","()(())","()()()"]

    输入: n = 1
    输出: ["()"]

约束:
    - 1 <= n <= 8
"""

from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []
    def dfs(prefix, left, right):
        if left == 0 and right == 0:
            result.append(prefix)
            return

        if left > 0:
            dfs(prefix + '(', left-1, right+1)
        if right:
            dfs(prefix + ')', left, right-1)
    dfs("", n, 0)
    return result


# ─────────────────────────── 测试框架 ───────────────────────────

def is_valid(s: str) -> bool:
    """验证括号字符串是否合法。"""
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0


# 卡特兰数：n 对括号的合法组合数
CATALAN = [1, 1, 2, 5, 14, 42, 132, 429, 1430]


def run_tests():
    test_cases = [
        (1, ["()"], "n=1"),
        (2, ["(())", "()()"], "n=2"),
        (3, ["((()))","(()())","(())()","()(())","()()()"], "n=3"),
    ]

    passed = 0
    failed = 0

    # 精确内容测试
    for n, expected, desc in test_cases:
        result = generateParenthesis(n)

        if result is None:
            print(f"FAIL [{desc}]: 返回 None")
            failed += 1
            continue

        got_sorted = sorted(result)
        exp_sorted = sorted(expected)

        if got_sorted != exp_sorted:
            print(f"FAIL [{desc}]: 期望 {exp_sorted}，实际 {got_sorted}")
            failed += 1
        else:
            print(f"PASS [{desc}]: {got_sorted}")
            passed += 1

    # 数量+合法性测试（n=4..8）
    for n in range(4, 9):
        result = generateParenthesis(n)
        desc = f"n={n}"

        if result is None:
            print(f"FAIL [{desc}]: 返回 None")
            failed += 1
            continue

        expected_count = CATALAN[n]

        if len(result) != expected_count:
            print(f"FAIL [{desc}]: 期望 {expected_count} 个，实际 {len(result)} 个")
            failed += 1
            continue

        # 检查无重复
        if len(result) != len(set(result)):
            print(f"FAIL [{desc}]: 结果含重复")
            failed += 1
            continue

        # 检查每个字符串合法
        invalid = [s for s in result if not is_valid(s)]
        if invalid:
            print(f"FAIL [{desc}]: 含非法括号串: {invalid[:3]}")
            failed += 1
            continue

        print(f"PASS [{desc}]: {expected_count} 个合法括号串")
        passed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败 / {passed + failed} 总计")


if __name__ == "__main__":
    run_tests()
