# Postfix to Prefix Expression

def push(x):
    global stack
    global top
    top += 1
    stack[top] = x
def pop():
    global stack
    global top
    x = stack[top]
    top -= 1
    return x
def is_operator(x):
    if x == '+' or x == '-' or x == '*' or x == '/':
        return True
    else:
        return False
def convert():
    global stack
    global top 
    l = len(exp)
    for i in range(0, l):
        if is_operator(exp[i]) == True:
            op1 = stack[top]
            pop()
            op2 = stack[top]
            pop()
            tmp = exp[i] + op2 + op1
            push(tmp)
        else:
            push(exp[i])
    print("The prefix expression is: ", stack[top])

stack = []
top = -1
exp = input("Enter the postfix expression: ")
for i in range(50):
    stack.append(0)
convert()