from collections import deque

def check_brackets_balance(file_path):
    opening_brackets = '['
    closing_brackets = ']'
    bracket_pairs = {'[': ']', '{': '}', '(': ')'}

    brackets_deque = deque()

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            for char in line:
                if char == opening_brackets:
                    brackets_deque.append((char, line_number))
                elif char == closing_brackets:
                    if not brackets_deque:
                        print(f"Ошибка: Нет соответствующей открывающей скобки для ']' на строке {line_number}.")
                        return False
                    last_opening_bracket, last_line_number = brackets_deque.pop()
                    if bracket_pairs[last_opening_bracket] != char:
                        print(f"Ошибка: Несоответствие скобок '{last_opening_bracket}' и '{char}' на строке {last_line_number}.")
                        return False

    if brackets_deque:
        last_opening_bracket, last_line_number = brackets_deque.pop()
        print(f"Ошибка: Нет соответствующей закрывающей скобки для '{last_opening_bracket}' на строке {last_line_number}.")
        return False

    return True

# Пример использования
file_path = 'program2.txt'  # Укажите путь к файлу с программой
if check_brackets_balance(file_path):
    print("Скобки сбалансированы.")
else:
    print("Скобки не сбалансированы.")
