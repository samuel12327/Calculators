print("Welcome to Drop Down Calculator!")
print("Insert Numbers in Integers or Operation Symbols Below: ")
print("Operation Symbol = + - / *")
def push(stack, value):
    stack.append(value)
def checkstack(stack):
    if (len(stack)<2):
        print("Please insert more than 1 number")
        return False
    else:
        return True
def add(stack):
    x = stack.pop()
    y = stack.pop()
    result = x + y
    push(stack, result)
    return result
def subtract(stack):
    x = stack.pop()
    y = stack.pop()
    result = y - x
    push(stack, result)
    return result
def divide(stack):
    x = stack.pop()
    y = stack.pop()
    result = y / x
    push(stack, result)
    return result
def multiply(stack):
    x = stack.pop()
    y = stack.pop()
    result = x * y
    push(stack, result)
    return result
stack = []
while True:
    insert = input("")
    if (insert=="+"):
        if(checkstack(stack)==True):
            print(add(stack))
        else:
            print("Add Number: ")
    elif (insert=="-"):
        if(checkstack(stack)==True):
            print(subtract(stack))
        else:
            print("Add Number: ")
    elif (insert=="/"):
        if(checkstack(stack)==True):
            print(divide(stack))
        else:
            print("Add Number: ")
    elif (insert=="*"):
        if(checkstack(stack)==True):
            print(multiply(stack))
        else:
            print("Add Number: ")
    else:
        push(stack, int(insert))



