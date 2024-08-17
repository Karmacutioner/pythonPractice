#Luke_Burgie_CSC20191N2_CH2-EX10
#Ingrident Adjuster Program
sugar = .03125 #for 1 cookie, measured in cups
butter = .020833333333 #for 1 cookie, measured in cups
flour = .0572916666666 #for 1 cookie, measured in cups
print('How many cookies do you want to make?')
desiredQuantity = float(input())
totalSugar=sugar*desiredQuantity
totalButter= butter*desiredQuantity
toatlFlour= flour*desiredQuantity
print(f'You will need {totalSugar:.2f} cups of sugar.')
print(f'You will need {totalButter:.2f} cups of butter.')
print(f'You will need {toatlFlour:.2f} cups of flour.')
