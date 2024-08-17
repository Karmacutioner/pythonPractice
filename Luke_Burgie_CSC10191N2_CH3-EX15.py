#Luke_Burgie_CSC10191N2_CH3-EX15
#Time Calculator
print('Input Seconds')
seconds = int(input())
if seconds < 60:
    print(f'{seconds} seconds')
elif seconds >= 60 and seconds < 3600:   
    remainderS = int(seconds % 60)
    minutes = int((seconds - remainderS)  / 60)
    print(f'{minutes} minutes {remainderS} seconds.' )
elif seconds >= 3600 and seconds < 86400:
    remainderM = seconds % 3600
    hours = int((seconds - remainderM) / 3600)
    remainderS = int((remainderM % 60))
    minutes = int((remainderM - remainderS) / 60)
    print(f'{hours} hours {minutes} minutes {remainderS} seconds')
else:
    remainderH = seconds % 86400
    days = int((seconds - remainderH) / 86400)
    remainderM = remainderH % 3600
    hours = int((remainderH - remainderM) / 3600)
    remainderS = int(remainderM % 60)
    minutes = int((remainderM-remainderS) / 60)
    print(f'{days} days {hours} hours {minutes} minutes {remainderS} seconds.')
