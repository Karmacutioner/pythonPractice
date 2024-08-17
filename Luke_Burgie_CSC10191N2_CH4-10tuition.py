#Luke_Burgie_CSC10191N2_CH4-10tuition
tuition = 8000
for year in range(1,6):
  tuition += (tuition *.03)
  print(f'For year {year} tuition will be ${tuition:.2f} each semester.')
