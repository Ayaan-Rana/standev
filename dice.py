import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

diceResult=[]
count=[]

for i in range(0,1000):
    dice1 = random.randint(1,6)

    dice2 = random.randint(1,6)

    diceResult.append(dice1+dice2)
    count.append(i)

mean= sum(diceResult)/len(diceResult)
stanDev=statistics.stdev(diceResult)
print(mean)
median=statistics.median(diceResult)
print(median)
mode=statistics.mode(diceResult)
print(mode)

fig=ff.create_distplot([diceResult],['result'],show_hist=False)
fig.show()

first_start_sd, first_end_sd = mean-stanDev, mean+stanDev
second_start_sd, second_end_sd = mean-(2*stanDev), mean+(2*stanDev)
print('{}% of data lies within one standard deviation, format(len())')