import plotly.express as px
import csv 
import numpy as np

with open("tempVsIceCream.csv") as csv_file :
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Ice-cream Sales(rs)")
    fig.show()

def getDataSource(data_path):
    temperature = []
    icecream_sales= []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row["Ice-cream Sales(rs)"]))
            temperature.append(float(row["Temperature"]))
        
    return{"x": icecream_sales, "y" : temperature}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation between temperature vs ice cream sales -- \n -> ", correlation[0, 1])

def setup():
    data_path = "tempVsIceCream.csv"
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()