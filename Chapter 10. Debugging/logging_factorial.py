import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.disable(logging.CRITICAL) - to disable logging messages
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial( %s)' % n)
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial( %s)' % n)
    return total


print(factorial(5))
logging.debug('End of program')

# LOGGING LEVELS

# DEBUG - The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
# INFO - to record information on general events in your program or confirm that things are working at their point in the program.
# WARNING - Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
# ERROR - Used to record an error that caused the program to fail to do something.
# CRITICAL - The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.