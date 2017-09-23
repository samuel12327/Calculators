print("Welcome to Stack Calculator")
print("Pick an Operation: add, sub, divide, multiply")
lists = []
oper = input("Enter Operation: ")
no1 = int(input("First Number: "))
no2 = int(input("Seoond Number: "))

def operation (lists, oper, no1, no2):
    lists.append(no1)
    lists.append(no2)
    lists.pop()
    lists.pop()
    if (oper == "add"):
        result = no2 + no1
    elif(oper == "sub"):
        result = no1 - no2
    elif (oper == "divide"):
        result = no1 / no2
    elif (oper == "multiply"):
        result = no2 * no1
    lists.append(result)
    return int(result)
print(operation (lists, oper, no1, no2))

def nthoperation (lists, oper, no2):
    lists.append(no2)
    no2 = lists.pop()
    no3 = lists.pop()
    if (oper == "add"):
        result = no3 + no2
    elif(oper == "sub"):
        result = no3 - no2
    elif (oper == "divide"):
        result = no3 / no2
    elif (oper == "multiply"):
        result = no3 * no2
    lists.append(result)
    return int(result)
then = input("Would you like to do anything else with the previous number? yes/no")
while then == "yes":
    oper = input("Enter Operation: ")
    no3 = int(input("Next Number"))
    print(nthoperation (lists, oper, no3))
    then = input("Would you like to do anything else with the previous number? yes/no")
else:
    print("Thank You for Using Stack Calculator!!")







