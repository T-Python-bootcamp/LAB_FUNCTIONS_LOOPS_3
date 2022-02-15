def find_primes(x:int, y:int):
    for num in range(x,y):
        for n in range(2,num):
            if (num % n == 0):
                break
        else:
            print(num)

find_primes(25, 50)