def  find_primes(x:int, y:int):
    result = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, (i//2)+1):
                if i % j == 0:
                    break
            else:
                result.append(i)
    return result

print(find_primes(25,50)) 