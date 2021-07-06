import csv
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()


mean=statistics.mean(data)
stdv=statistics.stdev(data)
print('The population mean is:', mean)
print('The population deviation is:', stdv)

# to find the mean of 100 data points 1000 times
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value= data[random_index]
        dataset.append(value)
    mean= statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean= random_set_of_mean(100)
    mean_list.append(set_of_mean)

standev=statistics.stdev(mean_list)
mean2=statistics.mean(mean_list)

print('The sampling mean is:', mean2)
print('The sampling dev is:', standev)

fig=ff.create_distplot([mean_list], ['Math score'], show_hist=False)
fig.add_trace(go.Scatter(x=[mean2,mean2]), y=[0,0.2],mode="lines", name="MEAN")
fig.show()

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean2-standev, mean2+standev
second_std_deviation_start, second_std_deviation_end = mean2-(2*standev), mean2+(2*standev)
third_std_deviation_start, third_std_deviation_end = mean2-(3*standev), mean2+(3*standev)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()