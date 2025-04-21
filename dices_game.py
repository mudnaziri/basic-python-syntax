import random

def dice_roll(dice ):
    roll=[]
    for i in range(0 , dice):
     face = random.randint(0 , side)
     roll.append(face)
    return roll


dice = int(input("Must have atleast one dice: "))

if (dice <=0 ): 
   print("must have atleast one dice: ")
   quit()

side = 6

if (side <= 0):
    print("must have atleast one side: ")
    quit()

roll= dice_roll(dice )

print(roll)


