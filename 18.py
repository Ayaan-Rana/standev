import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('data.csv')

heightList=df['Height(Inches)'].to_list()
weightList=df['Weight(Pounds)'].to_list()

heightMean=statistics.mean(heightList)
weightMean=statistics.mean(weightList)

heightMedian=statistics.median(heightList)
weightMedian=statistics.median(weightList)

heightMode=statistics.mode(heightList)
weightMode=statistics.mode(weightList)

stanDevHeight=statistics.stdev(heightList)
stanDevWeight=statistics.stdev(weightList)

print('mean, median and mode of height is {}, {} and {} respectively'.format(heightMean,heightMedian,heightMode))
print('mean, median and mode of weight is {}, {} and {} respectively'.format(weightMean,weightMedian,weightMode))

height_start_stanDev_first, height_end_stanDev_first= heightMean-stanDevHeight, heightMean+stanDevHeight
height_start_stanDev_second, height_end_stanDev_second= heightMean-(2*stanDevHeight), heightMean+(2*stanDevHeight)
height_start_stanDev_third, height_end_stanDev_third= heightMean-(3*stanDevHeight), heightMean+(3*stanDevHeight)

weight_start_stanDev_first, weight_end_stanDev_first= weightMean-stanDevWeight, weightMean+stanDevWeight
weight_start_stanDev_second, weight_end_stanDev_second= weightMean-(2*stanDevWeight), weightMean+(2*stanDevWeight)
weight_start_stanDev_third, weight_end_stanDev_third= weightMean-(3*stanDevWeight), weightMean+(3*stanDevWeight)

height_list_data_within_1standev=[result for result in heightList if result > height_start_stanDev_first and result < height_end_stanDev_first]
height_list_data_within_2standev=[result for result in heightList if result > height_start_stanDev_second and result < height_end_stanDev_second]
height_list_data_within_3standev=[result for result in heightList if result > height_start_stanDev_third and result < height_end_stanDev_third]

weight_list_data_within_1standev=[result for result in weightList if result > weight_start_stanDev_first and result < weight_end_stanDev_first]
weight_list_data_within_2standev=[result for result in weightList if result > weight_start_stanDev_second and result < weight_end_stanDev_second]
weight_list_data_within_3standev=[result for result in weightList if result > weight_start_stanDev_third and result < weight_end_stanDev_third]

print('mean, median and mode of height is {}, {} and {} respectively'.format(height_list_data_within_1standev,height_list_data_within_2standev,height_list_data_within_3standev))
print('mean, median and mode of weight is {}, {} and {} respectively'.format(weight_list_data_within_1standev,weight_list_data_within_2standev,weight_list_data_within_3standev))