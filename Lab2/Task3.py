class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def move_disks(n, source, target, auxiliary):
    if n == 1:
        disk = source.pop()
        target.push(disk)
        print(f"Переместить диск {disk} со стека {source} на стек {target}")
    else:
        move_disks(n-1, source, auxiliary, target)
        move_disks(1, source, target, auxiliary)
        move_disks(n-1, auxiliary, target, source)

# Создаем стеки для каждого стержня
stack_A = Stack()
stack_B = Stack()
stack_C = Stack()


with open('disks.txt', 'r') as file:
    for line in file:
        disk_size = int(line.strip())
        stack_A.push(disk_size)

# Перемещаем диски со стержня A на стержень C, используя стержень B в качестве промежуточного
move_disks(len(stack_A.items), stack_A, stack_C, stack_B)
