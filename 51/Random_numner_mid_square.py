def random(seed):
    seed = pow(seed,2)
    seed = seed//100
    seed = seed%10000
    return seed
def Main():
    seed = input()
    seed = int(seed)
    output = []
    n = 500
    while(n and seed):
        seed = random(seed)
        output.append((seed))
        n-=1
    print(output)


Main()
