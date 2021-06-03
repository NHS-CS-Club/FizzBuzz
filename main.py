number = int(input("Enter Number to test FizzBuzz Game: "))
while number > 0:
    if number % 3 == 0 and number % 5 != 0:
        print(str(number) +": Fizz")
    elif number % 5 == 0 and number % 3 != 0: 
        print(str(number) +": Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print(str(number) +": FizzBuzz")
    else:
        print(str(number))
    elif number % 7 == 0
        print(str(number) +": nobody likes multiples of 7")
    if number % 9 == 0:
        print(str(number) +": wow I guess")
    number-=1
