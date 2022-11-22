import sys
from datetime import datetime


original_write = sys.stdout.write

# Task 1
def my_write(string_text):
    if string_text != '\n':
        now = str(datetime.today()).split('.')[0]
        original_write(f'[{now}]: {string_text}')
    else:
        original_write('\n')


# Task 2
def timed_output(function):
    def wrapper(string):
        sys.stdout.write = my_write
        function(string)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


# Task 3
def redirect_output(filepath):
    def decorator(function):
        def wrapper():
            original_stdout = sys.stdout
            sys.stdout = open(filepath, 'a+')
            function()
            sys.stdout.close()
            sys.stdout = original_stdout

        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    sys.stdout.write = my_write
    # print('1, 2, 3')
    sys.stdout.write = original_write

    # print_greeting("Angelina")

    # calculate()
