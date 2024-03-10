def reverse_lines(input_file, output_file):
    stack = []

    # Читаем строки из исходного файла и добавляем их в стек
    with open(input_file, 'r') as file:
        for line in file:
            stack.append(line.strip())

    # Записываем строки из стека в обратном порядке в новый файл
    with open(output_file, 'w') as file:
        while stack:
            file.write(stack.pop() + '\n')


input_file = 'input.txt'
output_file = 'output.txt'
reverse_lines(input_file, output_file)
