while True:
    print("calculator")
    print("1-addition")
    print("2-subtract")
    print("3-mutiply")
    print("4-divide")
    print("Enter a or A to exit")

    choice= input("please enter a choice:")
    if choice == "a" or choice == "A":
       break                                      
    num1 = float(input("enter number1:"))
    num2 = float(input("enter number2:"))

    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2))
    elif choice == "2":
         print(num1, "-", num2, "=", (num1-num2))
    elif choice == "3":                                    
        print(num1, "*", num2, "=", (num1*num2))
    elif choice == "4":
        if num2 == 0.0:
          print("lauura  infinity maa answer aeeg")
        else:
            print (num1, "/", num2, "=", (num1/num2))
    else:
        print("bakchodi nhi laura jitna optio maa hai select kar nahi to exit. shantpatti mat kar 🖕")