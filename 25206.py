#너의 평점은

totalGrade=0.0
totalCredit=0.0
grade_to_point = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0
}

for _ in range(20):
    subject, credit, grade=input().split()
    credit=float(credit)
    if grade=='P':
        continue
    totalCredit+=credit
    totalGrade+=grade_to_point[grade]*credit

print(totalGrade/totalCredit)