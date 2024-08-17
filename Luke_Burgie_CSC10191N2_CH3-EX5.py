#Luke_Burgie_CSC10191N2_CH3-EX5
#Mass Calculator
print('Enter the mass of your object in kilograms.')
mass = float(input())
newtons = mass * 9.8
if 100 > newtons:
    print('Your object is too light!')
elif newtons > 500:
    print('Your object is too heavy!')
else:
    print(f'Your object weighs {newtons:.1f} newtons!') 
