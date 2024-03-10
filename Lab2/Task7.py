from collections import deque

def print_numbers_by_sign(file_path):
    numbers_deque = deque()

    with open(file_path, 'r') as file:
        for line in file:
            for num_str in line.split():
                num = int(num_str)
                if num < 0:
                    numbers_deque.appendleft(num)
                else:
                    numbers_deque.append(num)

    print("Отрицательные числа:")
    print_deque_contents(numbers_deque)
    print("Положительные числа:")
    print_deque_contents(numbers_deque)

def print_deque_contents(deque):
    while deque:
        print(deque.popleft() if deque[0] < 0 else deque.pop(), end=' ')
    print()


file_path = 'numbers.txt'
print_numbers_by_sign(file_path)
