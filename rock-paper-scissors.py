import random
user = None
while user is None :
    t = input("Enter 'r' or 's' or 'p' : \n ")
    if (t is 'r') or (t is 's') or (t is 'p') :
        user = t

pc = random.randint(1,3)
if pc is 1:
    print(" Computer : Rock")
elif pc is 2:
    print(" Computer : Paper")
else:
    print("Computer : Scissors")

if (user is 'r' and pc is 1) or (user is 'p' and pc is 2) or (user is 's' and pc is 3):
    print("Its a tie")
elif (user is 'r' and pc is 3) or (user is 's' and pc is 2) or (user is 'p' and pc is 1):
    print("User wins!")
else:
    print("Computer wins!")
    
    
