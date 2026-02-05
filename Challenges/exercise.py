#Keeps track of the amount of prime numbers the user enters
num = int(input("Enter a positive value: -1 to quit"))
primeCount = 0
isPrime = True
while num > 0:
  if num > 0:
    for i in range(1, num):
      if num % i == 0:
        isPrime = False
  if isPrime:
    print(num, "is prime")
    primeCount += 1
  else:
    print(num, "is not prime")
  num = int(input("Enter a positive value: -1 to quit"))

print("Prime Count: ", primeCount)