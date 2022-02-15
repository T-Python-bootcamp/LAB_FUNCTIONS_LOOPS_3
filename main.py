def find_primes(i: int, j: int):
    for n in range(i, j):
        if n % 2:
            if n % 3:
                if n % 5:
                    if n % 7:
                        if n % 11:
                            print(n)
            
find_primes(25, 50)