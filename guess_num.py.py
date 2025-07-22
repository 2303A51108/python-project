print("welcome the number guessing game ")
secret = 7;
num = int(input("enter the num:"))
if(num==secret):
    print("correct")
elif (num<secret):
    print("too small")
else:
    print("not correct")
    
