def is_matched(expression):
    # { } -1 1
    # [ ] -2 2
    # ( ) -3 3
    nor_exp = list(map(lambda x: convert(x), expression))
    stack = []
    for ele in nor_exp:
        if len(stack) == 0:
            stack.append(ele)
        else:
            top = stack[-1]
            if ele + top == 0:
                stack.pop()
            else:
                stack.append(ele)
    return len(stack) == 0


def convert(br):
    if br == "{":
        return -1
    if br == "}":
        return 1
    if br == "[":
        return -2
    if br == "]":
        return 2
    if br == "(":
        return -3
    if br == ")":
        return 3


exps = [
    '{[()]}',
    '{[(])}',
    '{{[[(())]]}}']

for exp in exps:
    print(is_matched(exp))
