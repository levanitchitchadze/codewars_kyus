"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

from codewars_kyus.utils.execution_counter import ex_time


@ex_time
def descending_order(num):
    #     solution #1
    #     res=0
    #     for d in sorted(str(num), reverse=True):
    #         res = res * 10 + int(d)
    #     return res

    #   solution #2
    return int("".join(sorted(str(num), reverse=True)))
