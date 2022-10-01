# #Write your code below this line 👇

# from math import ceil


# def paint_calc(height, width, cover):
#   calculation = ceil((height * width) / cover)
  
#   print(f"You will need {calculation} cans of paint.")





# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Write your code below this line 👇

def prime_checker(number):
  if number > 3:
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
      print(f"{number} is not a prime number.")
    else:
      print(f"{number} is a prime number.")
  else:
    print(f"{number} is a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



