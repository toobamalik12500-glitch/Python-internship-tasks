# TASK 6 – Student Performance Data Analysis

# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt


# Create student data
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zahra", "Usman"],
    "Roll Number": [1, 2, 3, 4, 5],
    "Subject": ["Python", "Python", "Python", "Python", "Python"],
    "Marks": [85, 72, 39, 91, 68],
    "Attendance": [90, 85, 70, 95, 80]
}


# Create DataFrame
df = pd.DataFrame(data)


# Save data to CSV file
df.to_csv("student_data.csv", index=False)


# Read data from CSV file using pandas
df = pd.read_csv("student_data.csv")


# Display all students
print("===== Student Performance Analysis =====")
print()
print(df)


# Calculate average marks
average_marks = df["Marks"].mean()


# Find highest marks
highest_marks = df["Marks"].max()


# Find lowest marks
lowest_marks = df["Marks"].min()


# Count passing students
passing_students = df[df["Marks"] >= 50]


# Count failing students
failing_students = df[df["Marks"] < 50]


# Find top student
top_student = df.loc[df["Marks"].idxmax(), "Name"]


# Display basic analysis
print()
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print()
print("Passing Students:", len(passing_students))
print("Failing Students:", len(failing_students))

print()
print("Top Student:", top_student)


# Intermediate Level

# Add grades
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


df["Grade"] = df["Marks"].apply(get_grade)


# Display grades
print()
print("Student Grades:")
print(df)


# Find Top 3 students
top_3_students = df.sort_values("Marks", ascending=False).head(3)

print()
print("Top 3 Students:")
print(top_3_students)


# Find students above 80 marks
students_above_80 = df[df["Marks"] > 80]

print()
print("Students Above 80 Marks:")
print(students_above_80)


# Advanced Level

# Save analyzed data to a new CSV file
df.to_csv("student_analysis.csv", index=False)

print()
print("Analyzed data saved to student_analysis.csv")


# Attendance analysis
average_attendance = df["Attendance"].mean()

print()
print("Average Attendance:", average_attendance)


# Subject-wise performance
subject_average = df.groupby("Subject")["Marks"].mean()

print()
print("Subject-wise Average Marks:")
print(subject_average)


# Create basic marks chart
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()


# Create basic attendance chart
plt.bar(df["Name"], df["Attendance"])

plt.title("Student Attendance")
plt.xlabel("Student Name")
plt.ylabel("Attendance")

plt.show()