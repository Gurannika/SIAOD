from collections import deque

def sort_lines(input_filename, output_filename):
    # Создаем два дека для хранения строк
    deck1 = deque()
    deck2 = deque()

    # Читаем строки из файла и добавляем их в первый дек
    with open(input_filename, 'r') as file:
        for line in file:
            deck1.append(line.strip())

    # Сортируем строки в первом деке
    deck1 = deque(sorted(deck1))

    # Перемещаем строки из первого дека во второй в алфавитном порядке
    while deck1:
        smallest = deck1.popleft()
        while deck2 and deck2[-1] < smallest:
            deck1.append(deck2.pop())
        deck2.append(smallest)

    # Записываем отсортированные строки из второго дека в новый файл
    with open(output_filename, 'w') as output_file:
        while deck2:
            output_file.write(deck2.popleft() + '\n')


input_filename = 'books.txt'
output_filename = 'new_books.txt'
sort_lines(input_filename, output_filename)
