import matplotlib.pyplot as ply
import csv
import string
import matplotlib.patches as mpa
import matplotlib.axes as axes

age = 1980
year = []
for k in range(0, 41):
  ages = str(age)
  year.append(ages)
  age = age + 1
print(year)

file = open("death.csv", "r")
dataIn = file.read()
file.close()
print(dataIn)

part = []
part = dataIn.split("\n")
part = part.pop(1)
part = part.split(",")
part = [str(item) for item in part]
print(part)
part = [elem.replace('r', '#EC1212') for elem in part]
part = [elem.replace('b', '#B4E4F3') for elem in part]
print(part)

value = []
value = dataIn.split("\n")
value = value.pop(0)
value = value.split(",")
value = [int(item) for item in value]
print(value)

#Create a line graph with names on x-axis and numbers on  y-axis

ply.bar(year, value, color=part)

ply.xlabel("years")

ply.ylabel("number of deathes")

fig, ax = ply.subplots()
Line1 = mpa.Patch(color='#4D26A2', label='Democrats')
Line2 = mpa.Patch(color='#A23D26', label='Republicans')
ax.legend(handles=[Line1, Line2])

# legend = ply.legend(['Democrats','Republicans'], title = "Policy party")

ply.show()
