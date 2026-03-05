from codewars_kyus.utils.execution_counter import ex_time


@ex_time
def palindrome(string: str):
    string = string.lower()
    return string == string[::-1]
