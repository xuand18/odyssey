

def postfix(eq):


    stack = []
    numList = []
    digitArr = [][]
    digitArrCount = 0
    digitCount = 0
    wasNum = False

    'N signifies the bottom of the stack. This can never be removed.'
    stack.append('N')

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
        def disp():
            print(stack)
            print(numList)
            print(digitArr)
            print(digitArrCount)
            print(digitCount)

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
            while stack[-1] != 'N' and (rank(eq[i]) <= rank(stack[-1])):
                wasNum = False
                digitArr[digitArrCount].append(digitCount)
                digitCount = 0
                digitArrCount = digitArrCount + 1
                numList.append(stack[-1])
                stack.pop()
            stack.append(eq[i])

    while stack[-1] != 'N':
        numList.append(stack[-1])
        stack.pop()


    return numList

print (postfix("48+96"))


