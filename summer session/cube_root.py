# import logging
# import sys


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
    print(f"Initial guess: {guess}")

    # Keep looping until we reach our desired accuracy. 
    while abs(guess ** 3 - number) > tolerance:
        # Use Newton's method to improve our guess.
        previous_guess = guess
        guess = (2 * guess + (number / (guess ** 2))) / 3
        if abs(guess-previous_guess) <= tolerance:
            break

        print(f"New guess: {guess}")

    print(f"Previous guess is solution")
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

    # logger = logging.getLogger('cube_root')
    # logger.addHandler(logging.StreamHandler(stream=sys.stderr))

    # the logging package defines these constants:
    #
    # logging.DEBUG:    10
    # logging.INFO:     20
    # logging.WARNING:  30
    # logging.ERROR:    40
    # logging.CRITICAL: 50
    #
    # each logging message has its own logging level. however, a logger also has a logging level that determines
    # whether it actually processes a log message. if the message has a log level that is at least as high as the
    # logger's current log level, then the message will be displayed (more correctly, it will be added to the log
    # stream).
    #
    # for example, if you tell a logger to log an INFO message but the logger's log level is WARNING, the message will
    # not be processed (and therefore it will not be displayed). an example that will process a log message would be if
    # you tell a logger to log an CRITICAL message and the logger's log level is ERROR.
    #
    # by default, a program's log level is set to WARNING, so log messages will be displayed if they have a log level
    # of WARNING, ERROR, or CRITICAL. if you change the program's log level to INFO, all log messages will be displayed
    # except for DEBUG messages.
    #
    # you can set each messages log level when you create it. to set the logger's log level, use its setLevel method.
    # you can change the logger's log level at any time.
    #
    # for production environments, you might read the logging level in from an environment variable or a configuration
    # file. here, for demonstration purposes, we will hard-code a value.
    #
    # the log messages for this program all have log level DEBUG, so if you sent log logger's log level to DEBUG in
    # following statement, you will see the log messages; otherwise, you will not.
    # logger.setLevel("WARNING")

    for fib_idx in range(1, 20):
        for tolerance_exp in range(10, -15, -1):
            target = fibonacci(fib_idx, fib_cache)
            tolerance = 10 ** tolerance_exp
            answer = cube_root(target, tolerance)
            print(f"The cube root of {target}, to within {tolerance}, is {answer}.")
