import plotly.express as px
import csv
import numpy as np

with open("sizeVsTime.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Size of TV", y ="\tAverage time spent watching TV in a week (hours)")
    fig.show()

def getDataSource(data_path):
    tvsize = []
    timeSpent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tvsize.append(float(row["Size of TV"]))
            timeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    
    return{"x": tvsize, "y": timeSpent}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation between the tv size and time spent watching -- \n -> ", correlation[0,1])

def setup():
    data_path = "sizeVsTime.csv"
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()