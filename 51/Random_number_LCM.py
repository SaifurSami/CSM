import numpy as np

def LCM(seed,a,c,mod):
    seed = (a*seed+c)%mod
    return seed

def main():
    seed = 1
    a = 13
    c = 0
    mod = 64
    n = 50 #maximum number
    random_numbers = []
    init = seed

    while(n):
        seed = LCM(seed,a,c,mod)
        random_numbers.append(seed)
        n-=1
        if seed == init:
            break
    print(random_numbers)

if __name__ == "__main__":
    main()