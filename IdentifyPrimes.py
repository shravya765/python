noprimes = [j for i in range(2,8) for j in range(i * 2,50, i)]
primes = [ x for x in range(2, 50) if x not in noprimes]
print(primes)


# OR

noprimes = []
for i in range(2,50):
    for j in range(i*2,50,i):
        noprimes.append(j)
primes = []
for x in range(2,50):
    if x not in noprimes:
        primes.append(x)
print(primes)