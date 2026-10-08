"""
Avengers List Operations
========================
A Python practice exercise on basic list operations using a Marvel theme.

Concepts covered:
    - len()     : counting items in a list
    - append()  : adding an item to the end of a list
    - pop()     : removing an item by index
    - insert()  : adding an item at a specific index
"""

# ---------------------------------------------------------------------------
# Task 1: Count the members of the Avengers team
# ---------------------------------------------------------------------------
# Question:
#   You are a Marvel fan and created a list of superheroes.
#   Using this list, calculate how many members are in the Avengers team.

avengers = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']

# len() returns the total number of items in the list
print("Task 1:")
print(f"Total {len(avengers)} members in the team!")

# Output:
# Total 6 members in the team!


# ---------------------------------------------------------------------------
# Task 2: Add a new member at the end of the list
# ---------------------------------------------------------------------------
# Question:
#   Iron Man made Spider-Man a new member of the Avengers.
#   Add him to the list at the end.

# append() adds a single item to the end of the list
avengers.append('Spider Man')

print("\nTask 2:")
print(avengers)

# Output:
# ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye', 'Spider Man']


# ---------------------------------------------------------------------------
# Task 3: Make Captain America the leader (move him before Iron Man)
# ---------------------------------------------------------------------------
# Question:
#   Everyone agreed that Captain America is the leader of the Avengers,
#   so place him before Iron Man.

# pop(1) removes the item at index 1 (Captain America) and returns it
captain_america = avengers.pop(1)

# insert(0, item) puts the item at the very front of the list (index 0)
avengers.insert(0, captain_america)

print("\nTask 3:")
print(avengers)

# Output:
# ['Captain America', 'Iron Man', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye', 'Spider Man']


# ---------------------------------------------------------------------------
# Task 4: Separate Hulk and Thor by moving Black Widow between them
# ---------------------------------------------------------------------------
# Question:
#   Thor and Hulk get angry easily and fight with each other.
#   Move "Black Widow" in between them to separate them.

# Black Widow is currently at index 2, so remove her from that position
black_widow = avengers.pop(2)

# After removal, Hulk is at index 2 and Thor is at index 3.
# Inserting at index 3 places Black Widow between Hulk and Thor.
avengers.insert(3, black_widow)

print("\nTask 4:")
print(avengers)

# Output:
# ['Captain America', 'Iron Man', 'Hulk', 'Black Widow', 'Thor', 'Hawkeye', 'Spider Man']
