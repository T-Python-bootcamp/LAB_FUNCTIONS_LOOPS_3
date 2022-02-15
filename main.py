

def all (num):
    temp=num-1
    while temp>1:
        if num % temp == 0:
            return False
        temp-=1
    return True

def find_primes(param1:int,param2:int):
    temp = list(range(param1,param2))
    primes=[]
    for x in temp:
        if not all(x):
            continue
        primes.append(x)
    return primes

print(find_primes(25,50))