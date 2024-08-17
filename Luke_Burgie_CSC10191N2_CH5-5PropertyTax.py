#Luke_Burgie_CSC10191N2_CH5-5PropertyTax
import math
print('Enter Property Value')
def assess_property(actualValue):
    assessedValue = actualValue * .6 #calculates assessment value at 60%
    tax = math.floor(assessedValue / 100) * .72 #calulates tax at $0.72 per $100
    print(f'Your assessment value is ${assessedValue:.2f} and you will pay ${tax:.2f} in taxes.')

assess_property(float(input()))
    
    
    

