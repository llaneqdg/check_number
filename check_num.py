check_num = int(input("Enter a number: "))

if check_num > 0:
    if check_num % 2 == 0:
        print("Positive Even Number.")
    else:
        print("Poitive Odd Number.")
else:
    print("Negative Number.")