print("Grades")

target = ("A or B")
grade = ("A or B")
number = int(input("What percentage did you get?"))

if (number > 50):
  print ("Your grade is A")
if (number < 50):
  print ("Your grade is B")

target = input("What was your target grade?")

while (target == grade):
  print("Well done you met your target")
  
if (target <= grade):
  print("Your grade was less than your target - please rebook your retest")
  
if (target >= grade):
  print("Well done you went above and beyond!")
  


