history =[]
while True:
    print("enter the choice \n 1 for calculator \n 2 for history \n 3 for deleting history \n 4 for exit")
    choice=int(input("enter the choice "))
    if choice==1:
        num1=int(input("enter the num1 "))
        num2=int(input("enter the num2 "))
        ope=input("enter the operation ")
        if ope=="+":
            result=num1+num2
            print("Addition = ",result)
        elif ope=="-":
            result=num1-num2
            print("Subtraction = ",result)
        elif ope=="*":
            result=num1*num2
            print("Multiplication = ",result)
        elif ope=="/":
            if num2==0:
                print("not possible ")
                continue
            result=num1/num2
            print("Division = ",result)
        else:
            print("invalid choice")
        history.append(f"{num1} {ope} {num2} = {result}")
    elif choice==2:
        if not history:
            print("history empty")
        else:
            print("history ")
            for item in history:
                print(item)
    elif choice==3:
        history.clear()
        print("history cleared ")
    elif choice==4:
        print("Exiting ")
        break 
    else:
        print("Invalid choice ")