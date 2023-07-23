from Stack import Stack

def balance_check(sequence):
    bracket_stack = Stack()
    for bracket in sequence:
            if bracket in ['(', '{', '[']:
                bracket_stack.push(bracket)
            else:
                if bracket == ')' and bracket_stack.peek() == '(':
                    bracket_stack.pop()
                elif bracket == '}' and bracket_stack.peek() == '{':
                    bracket_stack.pop()
                elif bracket == ']' and bracket_stack.peek() == '[':
                    bracket_stack.pop()
                else:
                    return 'Несбалансировано'
    if bracket_stack.is_empty():
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'
        

if __name__ == '__main__':
    sequence = input('Введите поседовательность скобок или \'y\' для выхода из программы: ')
    while sequence != 'y':
        print(balance_check(sequence))
        sequence = input('Введите поседовательность скобок или \'y\' для выхода из программы: ')