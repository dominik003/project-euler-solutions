upper_limit = 4000000


def get_even_fibonacci_numbers():
    left_pointer = 1
    right_pointer = 2

    limit_reached = False
    while not limit_reached:
        yield right_pointer

        for i in range(0, 3):
            old_left_pointer = left_pointer
            left_pointer = right_pointer
            right_pointer += old_left_pointer

        if right_pointer > upper_limit:
            limit_reached = True


even_fib_sum = 0
for fib_num in get_even_fibonacci_numbers():
    even_fib_sum += fib_num

print(even_fib_sum)
