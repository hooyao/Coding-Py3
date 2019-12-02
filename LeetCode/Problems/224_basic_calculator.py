import sys


# TODO cleanup code
class Solution:
    def calculate(self, s: str) -> int:
        clean_input = str.replace(s, ' ', '')
        number_stack = []
        symbol_stack = []
        symbols = ['(', ')', '+', '-']
        numbers = '0123456789'
        pos = 0
        while pos < len(clean_input):
            ele = clean_input[pos]
            if ele in numbers:
                tmp = int(ele)
                while pos + 1 < len(clean_input) and clean_input[pos + 1] in numbers:
                    tmp = tmp * 10 + int(clean_input[pos + 1])
                    pos += 1
                pos += 1
                if len(symbol_stack) == 0:
                    number_stack.append(tmp)
                    continue
                else:
                    if symbol_stack[-1] == '(':
                        number_stack.append(tmp)
                        continue
                    num = number_stack.pop()
                    symbol = symbol_stack.pop()
                    if symbol in ('+', '-'):
                        new_num = self.compute(num, tmp, symbol)
                        number_stack.append(new_num)
                    elif symbol == '(':
                        symbol_stack.append(symbol)
                    continue
            if ele in symbols:
                if ele in ('+', '-', '('):
                    symbol_stack.append(ele)
                elif ele == ')':
                    symbol_stack.pop()
                    if len(symbol_stack) > 0 and symbol_stack[-1] in ('+', '-'):
                        a = number_stack.pop()
                        b = number_stack.pop()
                        symbol = symbol_stack.pop()
                        new_num = self.compute(b, a, symbol)
                        number_stack.append(new_num)
                pos += 1
                continue
        if len(number_stack) == 2 and len(symbol_stack) == 1:
            return self.compute(number_stack[0], number_stack[1], symbol_stack[0])
        elif len(number_stack) == 1:
            return number_stack.pop()
        else:
            raise Exception('Something is wrong')

    def compute(self, a: int, b: int, symbol: str) -> int:
        if symbol == '+':
            return a + b
        elif symbol == '-':
            return a - b
        return None


def main(*args):
    solution = Solution()
    input = "(((1)+1-4+3))"
    input = "(1-(5-2))+1"
    result = solution.calculate(input)
    print(result)
    print(eval(input))


if __name__ == '__main__':
    main(*sys.argv[1:])
