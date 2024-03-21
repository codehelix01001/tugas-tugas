# Get the attendance grade
attendance = float(input("Enter your attendance grade: "))

# Get the assignment grade
assignment = float(input("Enter your assignment grade: "))

# Get the UTS grade
uts = float(input("Enter your UTS grade: "))

# Get the UAS grade
uas = float(input("Enter your UAS grade: "))

# Calculate the total grade
total_grade = attendance + assignment + uts + uas

# Determine the final grade
if total_grade >= 90:
    final_grade = "A"
elif total_grade >= 80:
    final_grade = "B"
elif total_grade >= 70:
    final_grade = "C"
elif total_grade >= 60:
    final_grade = "D"
else:
    final_grade = "E"

# Print the final grade
print("Your final grade is: ", final_grade)