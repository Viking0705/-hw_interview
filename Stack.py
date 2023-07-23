class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return bool(not self.stack)

    def push(self, new_element):
        self.stack.append(new_element)
        # print(f'В стек добавлен элемент: {new_element}\n')        

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def print_state(self):
        print(f'Состояние стека: {self.stack}\n')

def print_menu():
    print('     Меню:\n\
1. is_empty(). Проверка стека на пустоту (True - пуст, False - не пуст).\n\
2. push(new_element). Добавление нового элемента в стек.\n\
3. pop(). Удаление верхнего элемента стека.\n\
4. peek(). Верхний элемент стека.\n\
5. size(). Количество элементов в стеке.\n\
6. Вывод содержимого стека.\n\
Завершить работу? Для завершения введите \'y\'.\n')

    
def navigation(stack):
    print_menu()
    input_command = input('Введите номер команды: ')
    while input_command != 'y':
        if input_command == '1':
            print(f'Стек пуст? {stack.is_empty()}\n')
        elif input_command == '2':
            new_element = input('   - введите элемент для добавления в стек: ')
            stack.push(new_element)
        elif input_command == '3':
            print(f'Удален элемент стека: {stack.pop()}\n')
        elif input_command == '4':
            print(f'Верхний элемент стека: {stack.peek()}\n')
        elif input_command == '5':
            print(f'Количество элементов в стеке: {stack.size()}\n')
        elif input_command == '6':
            stack.print_state()
        print_menu()
        input_command = input('Введите номер команды: ')

if __name__ == '__main__':
    stack = Stack()
    navigation(stack)