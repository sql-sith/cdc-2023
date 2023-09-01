def cube_root(number, tolerance):
    """
    Finds the cube root of a number and lets the caller specify a tolerance 
    which indicates how accurate the answer needs to be.

    Parameters: 
        number (int or float): The number to find the cube root of. 
        tolerance (float): The maximum amount of error allowed in the answer. 

    Returns: 
        float: The cube root of the number, with an accuracy specified by the tolerance parameter. 
    """

    if number == 0:
        return 0

    numeric_sign = -1 if number < 0 else 1
    number = abs(number)

    # Set an initial guess for the cube root of the number. 
    guess = number / 3
    print(f"DEGUG: Initial guess: {guess}")

    # Keep looping until we reach our desired accuracy. 
    while abs(guess ** 3 - number) > tolerance:
        # Use Newton's method to improve our guess.
        previous_guess = guess
        guess = (2 * guess + (number / (guess ** 2))) / 3
        if abs(guess-previous_guess) <= tolerance:
            break

        print(f"DEGUG: New guess: {guess}")

    print(f"DEGUG: Previous guess is solution")
    return numeric_sign * guess


def fibonacci(term: int, cache: dict) -> int:
    """
        challenges:
            1. do memoization in a better way (preferably without passing in fib_cache)
            2. do memoization without recursion (supporting large values for term)

    """

    if term in cache.keys():
        return cache[term]
    else:
        cache[term] = fibonacci(term - 1, cache) + term
        return cache[term]


if __name__ == '__main__':
    global fib_cache
    fib_cache = {1: 1, 2: 2}

    for fib_idx in range(1, 20):
        for tolerance_exp in range(10, -15, -1):
            target = fibonacci(fib_idx, fib_cache)
            tolerance = 10 ** tolerance_exp
            answer = cube_root(target, tolerance)

            if logger is not None:
                logger.debug("yo")
            else:
                print(f"DEGUG: The cube root of {target}, to within {tolerance}, is {answer}.")
