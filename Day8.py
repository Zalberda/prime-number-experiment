def prime_checker(number):
  if number > 3:
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
      print(f"{number} is not a prime number.")
    else:
      print(f"{number} is a prime number.")
  else:
    print(f"{number} is a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)



