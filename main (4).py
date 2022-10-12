#Created by: Owen Whalley
#Created on: 2022/10/11

#asks the user what value is being multiplied by another value, and assigns it to the variables x and y.
x = int(input("What is your first variable? : "))
y = int(input("What is your second variable? : "))

#assign the value 0 to the answer variable.
answer = 0

#If both variables are negative, then evaluate them as positive. Else, they are evaluated normally.
if y < 0 and x < 0:
    y2 = y - y - y
    x2 = x - x - x
    for i in range(y2):
      answer += x2
      y2 -= 1
else:
  for i in range(y):
    answer += x
    y -= 1

#print the answer.
print("The answer is: "+str(answer))