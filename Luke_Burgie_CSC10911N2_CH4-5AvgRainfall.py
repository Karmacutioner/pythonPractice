#Luke_Burgie_CSC10911N2_CH4-5AvgRainfall
print('How many years do you want to track rainfall?')
years = int(input())
while years < 1:
     print('Time does not go backward. Try again.')
     years = int(input())
rain = 0
counter = 0

while counter < years:
   counter += 1
   for months in range(12):
    print('How much did it rain this month?')
    newRain = float(input())
    while newRain < 0:
     print('Rainfall cannot be negative.Try again')
     newRain = float(input()) 
    rain += newRain
print(f'Over {int(years*12)} months it rained {rain:.2f}", an avergae of {rain / (years * 12):.2f}" per month!')     
    
