# My entire life has gone into this humble project which you may use at your leisure.
# I would like to thank a few people for their contributions to this project:
# me, for coding
# me, for ideas
# me, for debugging
# [insert quote here]
numOneLoop = False
numTwoLoop = False
operationLoop = False
def add(firstnum, lastnum):
    print(firstnum + lastnum)
def subtract(firstnum, lastnum):
    print(firstnum - lastnum)
def multiply(firstnum, lastnum):
    print(firstnum * lastnum)
def divide(firstnum, lastnum):
    print(firstnum / lastnum)
print("Totally cool and awesome calculator!!!11!!")
numOne = int(input("Enter first number: "))
while numOneLoop == False:
    if isinstance(numOne, int) == False:
        print("Invalid input!")
    else:
        break
while numTwoLoop == False:
    numTwo = int(input("Enter second number: "))
    if isinstance(numTwo, int) == False:
        print("Invalid input")
    else:
        break
while operationLoop == False:
    operation = input("What do you want to do? Operations supported: +, -, *, /: ")
    if operation == "+":
        add(numOne, numTwo)
        break
    elif operation == "=":
        subtract(numOne, numTwo)
        break
    elif operation == "*":
        multiply(numOne, numTwo)
        break
    elif operation == "/":
        divide(numOne, numTwo)
        break
    else:
        print("Invalid input!")