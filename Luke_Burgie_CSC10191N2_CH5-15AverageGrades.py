#Luke_Burgie_CSC10191N2_CH5-15AverageGrades

def calc_average():
    avg = (s1 + s2 + s3 + s4 + s5) / 5 #calculate average score
    print(f'The average score is {avg:.2f}.')
    
def determine_grade(score): #convert score to grade
    if score >= 90:
        print('The grade is A')
    elif score >= 80:
        print('The grade is B')
    elif score >= 70:
        print('The grade is C')
    elif score >= 60:
        print('The grade is D')
    else:
        print('The grade is F')
        

s1 = float(input('Enter score')) #score input
determine_grade(s1)              #convert score to grade
s2 = float(input('Enter score')) #score input
determine_grade(s2)              #convert score to grade
s3 = float(input('Enter score')) #score input
determine_grade(s3)              #convert score to grade
s4 = float(input('Enter score')) #score input
determine_grade(s4)              #convert score to grade
s5 = float(input('Enter score')) #score input
determine_grade(s5)              #convert score to grade

calc_average()


    
