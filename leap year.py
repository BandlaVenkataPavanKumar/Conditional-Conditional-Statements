# leap year
a = int(input())
if a % 4 == 0:
    if a % 400 == 0:
        print(f'{a} is a leap year')
    elif a % 1000 == 0:
        print(f'{a} ia not a leap year')
    else:
        print(f'{a} is a leap year')
else:
    print(f'{a} not a leap year')
