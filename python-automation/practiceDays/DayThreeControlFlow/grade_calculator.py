# Grade Calculator Program

# Step 1: Take marks as input from the user for 5 subjects
print("Enter marks for 5 subjects (out of 100):")
subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

#Step 2: Calculate the total and average
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5

#Step 3: Display total and average
print("\nTotal Marks = ",total)
print("Average Marks = ",average)

# Step 4: Calculate and display grade based on average
# Grade criteria
# 90-100  => A+
# 80-89   => A
# 70-79   => B
# 60-69   => C
# 50-59   => D
# Below 50 => F

if average >=90:
    grade = "A+"
elif average >=80:
    grade = "A"
elif average >=70:
    grade = "B"
elif average >=60:
    grade = "C"
elif average >=50:
    grade = "D"
else:
    grade = "F"

#Step 5: Print the grade
print("Grade : ",grade)