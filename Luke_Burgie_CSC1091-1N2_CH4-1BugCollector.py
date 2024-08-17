#Luke_Burgie_CSC1091-1N2_CH4-1BugCollector
day = 1
totalBugs = 0
while day <= 5:
    print(f'How many bugs did you catch on day {day}?')
    bugsCaught = int(input())
    if bugsCaught < 0:
        print('You can\'t catch negative bugs! Try again!')
        bugsCaught = int(input()) 
    totalBugs += bugsCaught
    day += 1    
print(f'You caught {totalBugs} bugs!')     
