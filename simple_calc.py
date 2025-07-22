print("welcome to simple calculator")
num1 = int(input("enter you first num :"))

num2 = int(input("enter your second num2 :"))

print("choose the operator  + , - , / , *")
op = input("enter the operator :")

if op == "+" :
    print("answer is :", num1 + num2)
elif op == "-" :
    print("answer is :", num1 - num2)
elif op == "*" :
    print("answer is :", num1 * num2)
elif op == "/" :
    print("answer is :", num1 / num2)
else :
    print("sorry give it an another try! ")
