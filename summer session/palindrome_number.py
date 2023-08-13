# from math import log10, ceil
# import pandas as pd
# import matplotlib.pyplot as mp

from math import floor, log10


def is_palindrome(x: int) -> bool:

    if x < 0:
        return False
    elif x == 0:
        return True

    original_digits = floor(log10(x)) + 1
    original_digits_odd = (original_digits % 2 == 1)

    low_digits = 0
    for power10 in range(original_digits // 2):
        # capture low digits but reverse their order:
        low_digits = 10 * low_digits + (x % 10)
        x = x // 10

    if original_digits_odd:
        x = x // 10

    return x == low_digits

#
#     if x < 0:
#         return False
#     elif x == 0:
#         return True
#
#     digits = ceil(log10(x))
#     # adjust for exact powers of 10:
#     if x == 10 ** digits:
#         digits += 1
#
#     for idx in range(0, digits//2):
#         lo_digit = (x // 10 ** idx) % 10
#         hi_digit = (x // 10 ** (digits - idx - 1)) % 10
#
#         if hi_digit != lo_digit:
#             return False
#
#     return True


if __name__ == '__main__':

    for i in range(1000):
        # for n in 121, 10, 100021, 0, -5, 3, 111, 1112, 1211, 11, 111, 1324352413, 13243534231:
        for n in -2, 5, 11, 111, 111511, 123454321, 12341234123412341234123412344321432143214321432143214321:
            if is_palindrome(n):
                is_is_not = "is"
            else:
                is_is_not = "is not"

            print(f"{n} {is_is_not} a palindrome.")

    # nums_to_check = 100000000
    # sample_interval = 100000
    # palindromes_found_this_interval = 0
    # graph_data = []
    #
    # previous_palindrome = 0
    # for num in range(0, nums_to_check+1):
    #     if is_palindrome(num):
    #         graph_data.append({"palindrome": num, "palindrome gap": num - previous_palindrome})
    #         previous_palindrome = num
    #
    #     # if num % sample_interval == 0:
    #     #     graph_data[f"{num}"] = palindromes_found_this_interval
    #     #     palindromes_found_this_interval = 0
    #
    # print(graph_data)
    # df = pd.DataFrame(data=graph_data)
    # df.sort_values(by=['palindrome'], inplace=True)
    # df.plot(x='palindrome', y="palindrome gap", kind="line", marker='.')
    # print(df)
    # mp.show()

    # print(f"{palindromes_found} out of the first {nums_to_check} are palindromic.")

