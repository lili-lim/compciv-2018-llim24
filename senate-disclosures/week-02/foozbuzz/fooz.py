def fob(user_number):
    n = 1
    for n in range (user_number + 1):
        if n % 15 == 0:
            print(n, 'FizzBuzz')
        elif n % 3 == 0:
            print(n, 'Fizz')
        elif n % 5 ==0:
            print(n, 'Buzz')
        else:
            print(n)


