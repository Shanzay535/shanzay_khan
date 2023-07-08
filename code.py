eng_marks = int(input("Enter marks for English out of 100: "))
isl_marks = int(input("Enter marks for Islamiat out of 100: "))
maths_marks = int(input("Enter marks for Maths out of 100: "))

# Checking if marks are out of 100
if eng_marks > 100 or isl_marks > 100 or maths_marks > 100:
    print("Invalid input! Marks should be out of 100.")
    exit()

# Total marks
total_marks = 300

# Calculating percentage
obtained_marks = eng_marks + isl_marks + maths_marks
perc = (obtained_marks / total_marks) * 100

# Assigning grade based on percentage
if perc<=100 and perc>=80:
    print("grade= A+")
elif perc<=80 and perc>=70:
    print("grade= A")
elif perc<=70 and perc>=60:
    print("grade= B")
elif perc <= 60 and perc >= 50:
    print("grade= C")
elif perc <= 50 and perc >= 40:
    print("grade= D")
elif perc <= 40 and perc >= 33:
    print("grade= E")
elif perc <0 and perc >100:
    print("This is invalid percentage")
else:
    print("Fail")
# Displaying the result
print("Total Marks:", total_marks)
print("Obtained Marks:", obtained_marks)
print("Percentage:", perc)
#1
print("Twinkle, twinkle, little star,")
print("       How I wonder what you are!")
print("              Up above the world so high,")
print("              Like a diamond in the sky,")
print("Twinkle, twinkle, little star,")
print("       How I wonder what you are")

#2
import sys

print("Python Version:", sys.version)
#3
import datetime

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)
#4
import math

# Accepting the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Computing the area of the circle
area = math.pi * radius ** 2

# Displaying the area
print("The area of the circle is:", area)

#5
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = last_name+" "+first_name
print("Reversed name:", full_name)

#6
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
print("The addition is:", addition)

#7
def calculate_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'

# Taking input for subject marks
subject_marks = []
for i in range(5):
    subject = int(input(f"Enter marks for Subject {i+1}: "))
    subject_marks.append(subject)

# Calculating total marks and average marks
total_marks = sum(subject_marks)
average_marks = total_marks / len(subject_marks)

# Calculating grade
grade = calculate_grade(total_marks)

# Generating marksheet
print("************ Marksheet ************")
print("Subject\t\tMarks")
print("-------------------------------")
for i in range(5):
    print(f"Subject {i+1}\t\t{subject_marks[i]}")
print("-------------------------------")
print(f"Total Marks:\t{total_marks}")
print(f"Average Marks:\t{average_marks}")
print(f"Grade:\t\t{grade}")
print("***********************************")

#8
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")