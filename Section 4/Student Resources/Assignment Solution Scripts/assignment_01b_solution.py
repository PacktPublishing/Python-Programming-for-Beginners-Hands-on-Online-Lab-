# Assignment 1 Solution (Part 2)

# Subjects wit scores
# ** NOTE: Nothing is stopping you from entering - 101 or 120 or -20 or ten or london
english_score = int(input("Enter a score for English : \t"))
math_score = int(input("Enter a score for Math : \t\t"))
science_score = int(input("Enter a score for Science : \t"))
social_score = int(input("Enter a score for Social : \t\t"))

total = english_score + math_score + science_score + social_score

total_subjects = 4

average_score = total/total_subjects

# This is not the best way to format output.
# We will learn more when learning about strings.
print()
print("**************************")
print("       Result")
print("**************************")
print(" Total : \t\t", total)
print(" Average : \t\t", average_score)