def print_characters_by_type(file_path):
    digit_stack = []
    letter_stack = []
    other_stack = []

    with open(file_path, 'r') as file:
        for char in file.read():
            if char.isdigit():
                digit_stack.append(char)
            elif char.isalpha():
                letter_stack.append(char)
            else:
                other_stack.append(char)

    print("Цифры:")
    print_stack_contents(digit_stack)
    print("Буквы:")
    print_stack_contents(letter_stack)
    print("Остальные символы:")
    print_stack_contents(other_stack)

def print_stack_contents(stack):
    while stack:
        print(stack.pop(), end='')
    print()


file_path = 'symbols.txt'  # Укажите путь к файлу с символами
print_characters_by_type(file_path)
