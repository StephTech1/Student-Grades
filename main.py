#Write a program to ask a student their percentage mark and convert this to a grade - Conversion will be in a function called mark_grade
# ask the user for their target grade and print this with their mark
print("Grades")

mark_grade = ("A,B")
target = ("A,B")

number = int(input("What percentage did you get?"))

if (number > 50):
  print ("Your grade is A")
if (number < 50):
  print ("Your grade is B")

target = input("What was your target grade?")

while (target == ("A")):
  print("Well done you met your target")
  break
while (target < ("B")):
  print ("Your grade was less than your target - please rebook your retest")
  break
while (target > ("A")):
  print("Well done you went above and beyond!")

