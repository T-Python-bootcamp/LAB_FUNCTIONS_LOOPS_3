
def find_primes(num1:int,num2:int):
 for number in range(num1,num2):
    for n in range(2,number):
     if (number % n == 0):
        break
    else:
     print(number)
find_primes(25,50)    
