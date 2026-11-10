# creating a student grading sytem using if statement and else statement to determine whether the student has passed.
student_name = str(input("enter the student name"))
student_number = float(input("enter the student number"))
subject = input("enter subject name")
final_mark = int(input("enter the final mark"))
if final_mark < 0:
    raise ValueError("invalid mark")
elif final_mark > 100:
    raise ValueError("invalid mark")
elif final_mark >= 75:
    print("grade A, Pass")
elif final_mark > 70:
    print("Grade B, Pass")
elif final_mark > 60:
    print("Grade C, Pass")
elif final_mark > 50:
    print("Grade D, Pass")
else:
    print("Grade F, FAIL")
    

    