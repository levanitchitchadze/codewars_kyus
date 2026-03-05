from src.codewars_kyus.utils.execution_counter import ex_time


@ex_time
def two_sum(nums: list, target: int) -> list[int, int] | bool:
    if not nums or len(nums) < 2:
        raise RuntimeError('Invalid numbers list: list must be non-empty and needs to includes at least 2 numbers')

    seen = {}
    for i, n in enumerate(nums):
        if ind := seen.get(target - n):
            return [ind - 1, i]

        seen[n] = i + 1

    return False
