def isPrimeNumber (num:int):
    for number in range ( 2, num ):
        if ( num % number == 0 ):
            return False
    return num > 1

def find_prime (firstNumber:int, secondNumber:int):
    for number in range (firstNumber, secondNumber):
        if isPrimeNumber(number):
            print(number)

find_prime(25,50)
