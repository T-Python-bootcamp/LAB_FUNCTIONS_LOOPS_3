
def checkPrime(num:int):
    for n in range(2,num):
        if num % n == 0:
            return False
    
    return True

def find_primes(firstNum:int, secondNum:int):
    step = 1
    
    if firstNum >= secondNum:
        step = -1
    
    for num in range(firstNum,secondNum+1,step):
        if checkPrime(num) == True:
            print(num)
        else:
            continue

find_primes(25,50)