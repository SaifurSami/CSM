def linearCongruentialGenerator(a, b, seed, mod):
    randomNumbers = []
    val = seed

    while True:
        randomNumbers.append(val)
        val = (a * val + b) % mod
        if val == seed:
            break
    
    return randomNumbers

def showOutput(nums):
    for i in range(len(nums)):
        print(f"X{i} = {nums[i]}")
    

def main():
    multiplicativeConstant = 1
    additiveConstant = 3
    seed = 0
    mod = 10
    numbers = linearCongruentialGenerator(multiplicativeConstant, additiveConstant, seed, mod)
    showOutput(numbers)


if __name__ == "__main__":
    main()
