
def postfix(eq):
                        
    'Initializing variables'
    stack = []
    numList = []
    digitArr = []
    digitCount = 0
    wasNum = False

    'N signifies the bottom of the stack. This can never be removed.'
    stack.append('N')

    'This function determines which operation has priority'
    def rank(c):
        if c == '^':
            return 3
        if c == '*' or c == '/':
            return 2
        if c == '+' or c == '-':
            return 1
        else:
            return -1

    for i in range(0,len(eq)):

        if eq[i] == '(':
            stack.append(eq[i])
        elif eq[i].isdigit():
            if wasNum == True:
                digitCount = digitCount + 1
            else:
                digitCount = 1
                wasNum = True
            numList.append(eq[i])
        elif eq[i] == ")":
            while stack[-1] != 'N' and stack[-1] != '(':
                numList.append(stack[-1])
                stack.pop()
            if stack[-1] == '(':
                stack.pop()
        else:
            wasNum = False
            digitArr.append(digitCount)
            digitCount = 0
            while stack[-1] != 'N' and (rank(eq[i]) <= rank(stack[-1])):
                numList.append(stack[-1])
                stack.pop()
            stack.append(eq[i])
    digitArr.append(digitCount)
    while stack[-1] != 'N':
        numList.append(stack[-1])
        stack.pop()

    a = [numList, digitArr]
    return a


def modified_postfix(post, digit):
    modified = []
    i = 0
    while i < len(digit) and post != []:
        if post[0].isdigit():
            modified.append(post[0:digit[i]])
            post = post[digit[i]:]
            i=i+1
        else:
            modified.append(post[0])
            post = post[1:]
            i=i-1
    return modified


def eq_eval(mod, digit):
    new_post = []
    for i in range(0,len(mod)):
        new_post.append(''.join(mod[i]))
    i = 0
    while len(new_post) != 1:
        if new_post[i].isdigit():
            tempi=0
            i=i+1
        else:
            pop1 = int(new_post[i-2])
            pop2 = int(new_post[i-1])
            op = new_post[i]
            if op == '^':
                res = pop1 ** pop2
            elif op == '*':
                res = pop1 * pop2
            elif op == '/':
                res = pop1 / pop2
            elif op == '+':
                res == pop1 + pop2
            elif op == '-':
                res == pop1 - pop2
            else:
                print("Error in operation determination")
            'WHY THIS NO WORK'
            new_post[i-2] = str(res)
            new_post.pop(i)
            new_post.pop(i-1)
            i = 0  
    print(new_post)


a = postfix("123*2^10+1")
b = modified_postfix(a[0], a[1])
eq_eval(b, a[1])



