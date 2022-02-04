#These are the variables used for my randomised questions.
import random
num1=random.randint(1,50)
num2=random.randint(1,50)
num3=random.randint(1,50)
num4=random.randint(1,50)
num5=random.randint(1,50)
num6=random.randint(1,50)
num7=random.randint(1,50)
num8=random.randint(1,50)
num9=random.randint(1,50)
num10=random.randint(1,50)
#these varibales are for multiplication and subraction the top are for addition and subtraction.
num11=random.randint(1,12)
num12=random.randint(1,12)
num13=random.randint(1,12)
num14=random.randint(1,12)
num15=random.randint(1,12)
num16=random.randint(1,12)
num17=random.randint(1,12)
num18=random.randint(1,12)
num19=random.randint(1,12)
num20=random.randint(1,12)
#this is my start screen and the beginning of my guess counter.
guesss = 0
print ("----------NUMBER GUESSING GAME-----------")
print ("there will be 10 questions which include: multiplication, division, addition and subtraction")
#this is the format for all of my code it uses a random variable for each question and displays it. If you get the answer wrong it will repeat until you answer correctly which would break the code.If you answer wrong it will add one to the guess until you answer correctly which also adds a guess.
print ("What is?",num1, "+", num2,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num1 + num2):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num3, "+", num4,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num3 + num4):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num5, "+", num6,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num5 + num6):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num7, "-", num8,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num7 - num8):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num9, "-", num10,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num9 - num10):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num11, "times", num12,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num11 * num12):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question")
guesss += 1
print ("What is?",num13, "times", num14,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num13 * num14):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num15, "times", num16,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num15 * num16):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num17, "divided by (to the nearest whole number)", num18,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num17 // num18):
    print ("try again")
    guesss += 1
  else:
    break   
print ("Well done on to the next question") 
guesss += 1
print ("What is?",num19, "divided by (to the nearest whole number)", num20,)   
while True:
  guess = int(input("Answer here"))
  if guess != (num19 // num20):
    print ("try again")
    guesss += 1
  else:
    break
guesss += 1
print ("CONGRADULATIONS YOU FINISHED") 
#this was meant to be the rewards screen if you got above 80%.
if guesss == 12:
  print ("well done you got 80%")
elif guesss == 11:
  print ("AMAZING you got 90%")
elif guesss == 10:
  print (" POGGERS YOU GOT FULL MARKS... now i can finally leave this code. YOU WILL SWAP WITH ME HAHAHAHAHAHAHAHAHAHAHAHAHAHA (proceeds to suck you into the code)")
else:
  print (" you didnt even get 80% you need to try again")
#that is the end of my code. 