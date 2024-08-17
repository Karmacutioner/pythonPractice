#Luke_Burgie_CSC10191N2_CH5-20RandomNumberGame 
import random
def player_guess(guess):
    winningNumber = random.randint(1,100) #determine winning number
    count = 0                             #game counter
    win = False                           #determine win or lose 
    while win == False  :
        if guess == winningNumber:
         count += 1
         print(f'YOU WIN!!! It took you {count} guesses to win!')
         win = True                       #ends loop
        elif guess > winningNumber:
            count += 1
            print('Too high, try again.')
            guess = int(input())
        else:
            count += 1
            print('Too low, try again.')
            guess = int(input())
            

while 1 == 1:                            #restarts game after win
   player_guess(int(input('Guess a number between 1 and 100')))


    
