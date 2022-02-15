import math
def prim(num1:int,num2:int):
    for n in range(num1,num2):
        isPrim=True
        for x in range(1,n):
            if x!=1 and math.remainder(n, x)==0.0:
                isPrim=False
        if isPrim:
            print(n)
prim(25,50)