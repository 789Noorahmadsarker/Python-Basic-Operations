"""
Student Grade Summary
=====================
A Python practice exercise on categorizing scores into letter grades
and counting how many students fall into each grade.

Concepts covered:
    - for loops
    - if / elif / else conditions
    - Counter variables
    - f-string formatting
"""

# ---------------------------------------------------------------------------
# Task 7: Categorize scores into grades
# ---------------------------------------------------------------------------
# Question:
#   Categorize each score into a grade based on the following thresholds:
#       A: 90 to 100
#       B: 80 to 89
#       C: 70 to 79
#       D: 60 to 69
#       F: Below 60
#   Count the number of students in each grade category and print a summary
#   of how many students received each grade.

# Scores of the students (carried over from the previous list exercise)
scores = [92, 85, 76, 58, 89, 91, 73, 84, 83]

# Initialize a counter for each grade, all starting at 0
grade_A = grade_B = grade_C = grade_D = grade_F = 0

# Process each score in the list using a for loop
for score in scores:
    # Conditions are checked from the highest grade to the lowest.
    # Once a condition is true, the remaining elif/else blocks are skipped,
    # so there is no need to check an upper limit (e.g. score <= 100).
    if score >= 90:       # Condition for grade A
        grade_A += 1
    elif score >= 80:     # Condition for grade B
        grade_B += 1
    elif score >= 70:     # Condition for grade C
        grade_C += 1
    elif score >= 60:     # Condition for grade D
        grade_D += 1
    else:                 # Condition for grade F (below 60)
        grade_F += 1

# Print the grade summary
print("Grade Summary:")
print(f"- A: {grade_A} students")
print(f"- B: {grade_B} students")
print(f"- C: {grade_C} students")
print(f"- D: {grade_D} students")
print(f"- F: {grade_F} students")

# Output:
# Grade Summary:
# - A: 2 students
# - B: 4 students
# - C: 2 students
# - D: 0 students
# - F: 1 students
