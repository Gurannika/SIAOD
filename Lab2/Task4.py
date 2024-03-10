def check_brackets_balance(file_path):
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    brackets_map = {'(': ')', '{': '}', '[': ']'}
    line_number = 0

    with open(file_path, 'r') as file:
        for line in file:
            line_number += 1
            for char in line:
                if char in opening_brackets:
                    stack.append((char, line_number))
                elif char in closing_brackets:
                    if not stack:
                        print(f"Ошибка: Нет соответствующей открывающей скобки для '{char}' на строке {line_number}.")
                        return False
                    last_opening_bracket, last_line_number = stack.pop()
                    if char != brackets_map[last_opening_bracket]:
                        print(f"Ошибка: Несоответствие скобок '{last_opening_bracket}' и '{char}' на строке {last_line_number}.")
                        return False

    if stack:
        last_opening_bracket, last_line_number = stack.pop()
        print(f"Ошибка: Нет соответствующей закрывающей скобки для '{last_opening_bracket}' на строке {last_line_number}.")
        return False

    return True


file_path = 'program.txt'
if check_brackets_balance(file_path):
    print("Скобки сбалансированы.")
else:
    print("Скобки не сбалансированы.")
