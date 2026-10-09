"""
Student Scores: List Indexing and Slicing
=========================================
A Python practice exercise on accessing and updating list elements,
using students' exam scores as the data.

Concepts covered:
    - Positive indexing : scores[0]
    - Negative indexing : scores[-1]
    - Slicing           : scores[start:stop]
    - append()          : adding an item to the end of a list
"""

# ---------------------------------------------------------------------------
# Task 1: Access scores using indexing and slicing
# ---------------------------------------------------------------------------
# Question:
#   The list below contains the scores of students in a class, ordered by
#   roll number (the first element is roll # 1, the second is roll # 2, and
#   so on). Print the scores of:
#       1. The first student
#       2. The last student
#       3. The first 3 students
#       4. Roll # 3, 4 and 5

scores = [92, 85, 76, 58, 89, 91, 73, 84]

# 1. Score of the first student
# Python indexing starts at 0, so the first element is at index 0
print("Task 1:")
print("First student:", scores[0])

# Output:
# First student: 92


# 2. Score of the last student
# A negative index counts from the end of the list, so -1 is the last element
print("Last student:", scores[-1])

# Output:
# Last student: 84


# 3. Scores of the first 3 students
# Slicing syntax is [start:stop]. The start index is included and the stop
# index is excluded, so [:3] returns indexes 0, 1 and 2.
print("First 3 students:", scores[:3])

# Output:
# First 3 students: [92, 85, 76]


# 4. Scores of roll # 3, 4 and 5
# Roll # 3 is at index 2 (roll number - 1), and roll # 5 is at index 4.
# Since the stop index is excluded, we use [2:5] to include index 4.
print("Roll # 3, 4 and 5:", scores[2:5])

# Output:
# Roll # 3, 4 and 5: [76, 58, 89]


# ---------------------------------------------------------------------------
# Task 2: Add a new student's score
# ---------------------------------------------------------------------------
# Question:
#   We received the result of one more student, which is 83 marks.
#   Append this to the scores at the end and print the list.

# append() adds a single item to the end of the list
scores.append(83)

print("\nTask 2:")
print(scores)

# Output:
# [92, 85, 76, 58, 89, 91, 73, 84, 83]
