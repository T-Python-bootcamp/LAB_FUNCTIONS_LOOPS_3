

# Get Prime numbers between two parameters
def find_primes(num_1: int, num_2: int):
    primNumbers = range(num_1, num_2+1)
    for num in primNumbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


find_primes(25, 50)
