pin = 1234
print("pleas enter your pincode")
user_pin = int(input())

if pin==user_pin:
    print("how much do you want to withdraw")
else:
    print("error, please enter correct pincode, you have two attempts left")
    user_pin = int(input())
    if pin == user_pin:
        print("how much do you want to withdraw")
    else:
        print("error, please enter correct pincode, you have one attempts left")
        user_pin = int(input())
        if pin == user_pin:
            print("how much do you want to withdraw")
        else:
            print("error, please contact the bank")