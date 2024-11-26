
def is_opening(c):
    opening = ['(', '[', '{']
    return c in opening
    
def are_closing_pair(opening, closing):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return pairs[opening] == closing

def closed_parentheses(s):
    stack = []
    for c in s:
        if is_opening(c):
            stack.append(c)
        elif stack and are_closing_pair(stack[-1], c):
            stack.pop()
    return len(stack) == 0

s = "([])[]({})"
print(closed_parentheses(s)) # True

s= "([)]"
print(closed_parentheses(s)) # False
