"""
დაბეჭდე რიცხვები 1-დან 100-მდე, მაგრამ:
თუ რიცხვი იყოფა 3-ზე -> დაბეჭდე "Fizz"
თუ რიცხვი იყოფა 5-ზე -> დაბეჭდე "Buzz"
თუ იყოფა ორივეზე (3 და 5) -> დაბეჭდე "FizzBuzz"
სხვა შემთხვევაში -> დაბეჭდე თვითონ რიცხვი
"""

from codewars_kyus.utils.execution_counter import ex_time


@ex_time
def fizzbuzz(n):
    if n is None:
        raise RuntimeError("N can't be None")

    for i in range(1, n):

        if i % 15 == 0:
            print(f"{i}: FizzBuzz")
            continue

        if i % 3 == 0:
            print(f"{i}: Fizz")
            continue

        if i % 5 == 0:
            print(f"{i}: Buzz")
            continue

        print(i)


# Execution time: 11.3328330170 seconds
# Execution time: 10.8832440820 seconds

fizzbuzz(10000000)
