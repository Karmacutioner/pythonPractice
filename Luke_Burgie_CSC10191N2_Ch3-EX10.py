#Luke_Burgie_CSC10191N2_Ch3-EX10
#Money Counting Game
print('How many pennies do you have?')
p = float(input()) *.01 
print('How many nickels do you have?')
n = float(input()) *.05
print('How many dimes do you have?')
d = float(input()) * .10
print('How many quarters do you have?')
q = float(input()) * .25
if p + n + d + q == 1.00:
    print('Congratulations!! YOU WIN!!')
elif  p + n + d + q < 1.00:
    print('Sorry that is less than 1 dollar. Try again!')
else:
    print('Sorry that is more than 1 dollar. Try again!')
    
