import random as r
random_no=r.randint(1,100)
print("______________Welcome to number Guessing________________")
name=input("Enter your name:")
print("Hi " + name)
turns=1

while (turns<6):
 print("......................................................")
 guess=int(input("Enter any number between 1 to 100:"))
 turns =turns+1
 print(f'You have exausted 1 turn,remaining  {6-turns} chances left')

 if(guess==random_no):
   print("Congratulations! You Guessed Right :) ")
   break

 elif(guess>random_no):
   print("Hint:The Number is Smaller than Your Guessed Number")

 elif(guess<random_no):
  print("Hint:The Number is Greater than Your Guessed Number")

  if(random_no<30):
    print("number is less than 30")
  elif(random_no>15 and random_no<25):
     print("number is in range between 15 and 25")

  if(random_no>50 and random_no<75):
     print("number is less than 75 and greater than 50")

  elif(random_no>75 and random_no<100):
   print("number is in range between 75 and 100")

  if(random_no%2==0):
   print("It is an even number")

  else:
   print("It is an odd number")

   if(random_no%5==0):
     print("it is divisible of 5")
   
   else:
     print("Sorry you lost!")