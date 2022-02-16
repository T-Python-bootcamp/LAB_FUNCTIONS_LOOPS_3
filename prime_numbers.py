def func(n1: int, n2: int):
    primes = list(range(n1, n2))

    if n1 >= 2:
        for num1 in range(n1, n2):
            if num1 == 2:
                continue
            else: 
                for num2 in range(2, num1):
                    if num1 % num2 == 0 :
                        if num1 in primes:
                            primes.remove(num1)
        return primes
    else:
        print("First number should be greater than 1")
    

print(func(2, 40))