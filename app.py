def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def scholarship_eligible(marks, attendance):
    return marks >= 75 and attendance >= 75


if __name__ == "__main__":
    marks = 82
    attendance = 88

    grade = calculate_grade(marks)
    eligible = scholarship_eligible(marks, attendance)

    print("Student Marks:", marks)
    print("Attendance:", attendance)
    print("Grade:", grade)
    print("Scholarship Eligible:", eligible)
