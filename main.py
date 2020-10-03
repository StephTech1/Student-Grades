#Write a program to ask a student their percentage mark and convert this to a grade - Conversion will be in a function called mark_grade
# ask the user for their target grade and print this with their mark
print("Grades")
mark_grade = 0 
number = int(input("What percentage did you get?"))

if (number > 75):
  print ("Your grade is A")
if (number < 75):
  print ("Your grade is B")