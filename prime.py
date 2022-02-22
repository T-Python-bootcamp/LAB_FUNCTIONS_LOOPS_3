

def isPrime(num1:int , num2:int):
    primeList = []
    for i in range(num1 , num2):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2 , int(i/2) +1):
                if i % j == 0:
                    break
            else:
                primeList.append(i)
    return primeList
print(isPrime(25,50))