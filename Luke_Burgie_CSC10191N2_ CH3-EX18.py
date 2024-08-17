#Luke_Burgie_CSC10191N2_ CH3-EX18
#Restaurant Selector
print('Is anyone vegitarian? Enter Yes or No')
vegi = input()
print('Is anyone vegan? Enter Yes or No')
vegan = input()
print('Is anyone gluten free? Enter Yes or No')
gluten = input()
print('Corner Cafe')
print('The Chef\'s Kitchen') 
if vegi != 'yes' and vegan != 'yes' and gluten != 'yes':
    print('Joe\'s Gormet Burgers')
if vegan != 'yes' and gluten != 'yes':
    print('Mama\'s Fine Itailan')
if vegan != 'yes':
    print('Main Street Pizza Co.')
    
