from collections import deque

def process_file(input_file, output_file):
    negative_stack = deque()
    positive_stack = deque()

    with open(input_file, 'r') as file:
        for line in file:
            numbers = map(int, line.split())
            for num in numbers:
                if num < 0:
                    negative_stack.append(num)
                else:
                    positive_stack.append(num)

    print("Отрицательные числа:")
    while negative_stack:
        print(negative_stack.pop())

    print("\nПоложительные числа:")
    while positive_stack:
        print(positive_stack.popleft())

    with open(output_file, 'w') as output:
        output.write("Отрицательные числа:\n")
        while negative_stack:
            output.write(str(negative_stack.pop()) + "\n")

        output.write("\nПоложительные числа:\n")
        while positive_stack:
            output.write(str(positive_stack.popleft()) + "\n")

input_file = 'numbers.txt'
output_file = 'processed_numbers.txt'
process_file(input_file, output_file)

