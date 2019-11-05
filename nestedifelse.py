num = int(input("\n\n Enter your number: "))

if num >= 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")
