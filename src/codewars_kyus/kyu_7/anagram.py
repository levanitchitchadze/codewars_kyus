from codewars_kyus.utils.execution_counter import ex_time


@ex_time
def anagram(s, s2):
    return sorted(s) == sorted(s2)
