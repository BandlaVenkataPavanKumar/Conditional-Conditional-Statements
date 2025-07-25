print("Enter your cgpa semister wise")
sem1 = float(input("Enter your semester 1 CGPA: "))
sem2 = float(input("Enter your semester 2 CGPA: "))
sem3 = float(input("Enter your semester 3 CGPA: "))
sem4 = float(input("Enter your semester 4 CGPA: "))
sem5 = float(input("Enter your semester 5 CGPA: "))
sem6 = float(input("Enter your semester 6 CGPA: "))
sem7 = float(input("Enter your semester 7 CGPA: "))
sem8 = float(input("Enter your semester 8 CGPA: "))
total_cgpa = sem1 + sem2 + sem3 + sem4 + sem5 + sem6 + sem7 + sem8
final_cgpa = total_cgpa / 8
final_percentage = final_cgpa * 9.5
print(f"Your final cgpa is: {final_cgpa}\n + Your final percentage is: {final_percentage}")