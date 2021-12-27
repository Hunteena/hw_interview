class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def balanced_parenthesis(parenthesis: str) -> str:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    p_stack = Stack()
    for p in parenthesis:
        if p in pairs.values():
            p_stack.push(p)
        elif p in pairs.keys():
            if pairs[p] == p_stack.peek():
                p_stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    tests = [
        ('(((([{}]))))', 'Сбалансированно'),
        ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
        ('{{[()]}}', 'Сбалансированно'),
        ('}{}', 'Несбалансированно'),
        ('{{[(])]}}', 'Несбалансированно'),
        ('[[{())}]', 'Несбалансированно'),
        ('( )', 'Сбалансированно'),
        (')', 'Несбалансированно')
    ]
    for sequence, result in tests:
        assert balanced_parenthesis(sequence) == result
