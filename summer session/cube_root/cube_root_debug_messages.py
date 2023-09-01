import logging
import sys
import argparse

from typing import Dict

# globals
fib_cache = {}


def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging_level', type=str, nargs='?', default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'],
                        help='The logging level to use. Default is WARNING.')

    return parser.parse_args()


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
    logger.debug(f"Initial guess: {guess}")

    # Keep looping until we reach our desired accuracy. 
    while abs(guess ** 3 - number) > tolerance:
        # Use Newton's method to improve our guess.
        previous_guess = guess
        guess = (2 * guess + (number / (guess ** 2))) / 3
        logger.debug(f"New guess: {guess}")
        if abs(guess-previous_guess) <= tolerance:
            break

    logger.debug(f"Previous guess is solution")
    return numeric_sign * guess


def fibonacci(term: int) -> int:
    """
        to do:
            1. [done, 2023-08-17] do memoization in a better way (preferably without passing in fib_cache)
            2. [done, 2023-08-17] do memoization without recursion (supporting large values for term)

        bug fixes:
            1. [done, 2023-08-17] i apparently forgot the formula for the fibonacci sequence. oops. fixed.

    Returns:
        fib_cache[term]: int
    """
    global fib_cache
    if fib_cache == {} or fib_cache is None:
        fib_cache = {0: 0, 1: 1}

    if term in fib_cache.keys():
        return fib_cache[term]
    else:
        current_max_term = max(fib_cache.keys())
        for current_term in range(current_max_term, term):
            fib_cache[current_term + 1] = fib_cache[current_term] + fib_cache[current_term - 1]
        return fib_cache[term]


def start_main():
    cube_roots_calculated = 0

    for fib_idx in range(1, 20):
        for tolerance_exp in range(2, -3, -1):
            target = fibonacci(fib_idx)
            tolerance = 10 ** tolerance_exp
            answer = cube_root(target, tolerance)
            cube_roots_calculated += 1
            logger.debug(f"\nThe cube root of {target}, to within {tolerance}, is {answer}\n.")

    print(f"Successfully calculated the cube roots of {cube_roots_calculated} numbers.")


def configure_logger(logging_level) -> logging.Logger:
    new_logger = logging.getLogger('cube_root')
    new_logger.addHandler(logging.StreamHandler(stream=sys.stderr))
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
    new_logger.setLevel(logging_level)
    return new_logger


if __name__ == '__main__':

    # get logging level from command-line arguments and configure logging:
    args = get_parsed_args()
    logger = configure_logger(args.logging_level)
    start_main()
