import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv('newdata.csv')
data = df["temp"].tolist()


def random_set_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value= data[random_index]
        dataset.append(value)
    data_mean= statistics.mean(dataset)
    return data_mean



def show_fig(mean_list):
    df= mean_list
    fig=ff.create_distplot([df], ["temp"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean= random_set_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()
