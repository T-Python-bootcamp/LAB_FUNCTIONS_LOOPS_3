def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, (i//2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

print(prime(25,50))