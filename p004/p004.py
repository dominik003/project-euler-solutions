min_number = 10000
max_number = 99999


def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def yield_palindromes(min_possible_number=min_number**2, max_possible_number=max_number**2) -> [int]:
    for cur_num in range(max_possible_number, min_possible_number - 1, -1):
        if is_palindrome(cur_num):
            yield cur_num


for num in yield_palindromes():
    for x in range(max_number, min_number-1, -1):
        if min_number * x > num:
            continue

        for y in range(max_number, min_number-1, -1):
            res = x * y
            if res == num:
                print(f"Result found: {x} * {y} = {num}")
                exit()
            elif res < num:
                break
