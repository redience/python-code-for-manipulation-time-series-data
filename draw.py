import numpy#just I need to use numpy, matplotlib to draw this file.
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime#I tried to use date time, but I give up cause i can't make it show as i want.
import matplotlib.dates as mdate
is_first_line = True
line_number = 0
id = []
time = None
timein = []
ele = []
number = 0
elenumber = 0
max = 0
min = 9999
second = -1
values = []
average = 0
i = 0
for row in open("C:/Users/yangjianlei/Desktop/learning/data for an hour.csv"):#I got somepproblem of uploading file.
    # C:/Users/yangjianlei/Desktop/learning/data for an hour.csv
    if is_first_line:
        is_first_line = False#to make sure it doesn't read firstline.
    else:
        values = row.split(",")#split it to line.
        time = values[1]
        newtime = time.split(":")
        mc = newtime[1].split(".")
        # second = (float(newtime[0]) * 60) + float(mc[0]) + (float(mc[1]) * 0.1)
        second += 1#this file count the data every second, so i just use it.
        i += 1
        timein.append(second)
        elenumber = int(values[2])
        average += elenumber
        ele.append(elenumber)
        if elenumber > max:
            max = elenumber
            maxtime = second
        if elenumber < min:
            min = elenumber
            mintime = second
y = ele
x = timein
fig = plt.figure(figsize=(10, 20))
fig.suptitle("data for an hour")
plt.title("data for an hour")
plt.ylabel("ele")
plt.xlabel("time")
plt.plot(x,y)
print("in " + str(maxtime) + "second, the ele reaches the maximum " + str(max))
print("in " + str(mintime) + "second, the ele reaches the minimum " + str(min))
average = average/second
print('in this graph, the average of ele is {:.2f}'.format(average))
plt.show()
