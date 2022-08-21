from math import sqrt
primes = [3]
num = 5
prime = True

#Insert condition to genarate primes until:
  prime = True
  for i in range(len(primes)):
    while primes[i] <= sqrt(num):
      if num % primes[i] == 0:
        prime = False
        num += 2
        break
      break
  if prime == True:
    primes.append(num)
    num += 2

print(sum(primes) + 2)