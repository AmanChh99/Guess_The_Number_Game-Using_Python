import random
randomNumber = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess != randomNumber):
    userGuess = int(input("Enter a number: "))
    guesses +=1
    if(userGuess == randomNumber):
        print("You Guessed it right!")
    else:
        if(userGuess>randomNumber):
            print("You Guessed it wrong! Please Enter a smaller Number")
        else:
           print("You Guessed it wrong! Please Enter a larger Number") 

print(f"You Guessed the Number in {guesses} guesses")

with open("hiscore.txt",'r') as f:
    hiscore = int(f.read())
if(hiscore>guesses):
    print("Congratulations! You have broken the Hiscore")
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses))