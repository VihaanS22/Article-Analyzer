import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

print("")
print("Article Reading Time Analyzer")
print("")

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

p_mean = statistics.mean(data)
print("THE POPULATION MEAN IS ", p_mean)
print("")

stdev = statistics.stdev(data)
print("THE STDEV IS ", stdev)
print("")

def RandomSetOfMeans(counter):

    dataset = []
    for i in range(0, counter):
        randIndex = random.randint(1, len(data) - 1) 
        value = data[randIndex]
        dataset.append(value)

    t_mean = statistics.mean(dataset)
    return t_mean


def drawGraph(meanlist):

    sample_mean = statistics.mean(meanlist)
    print("THE SAMPLE MEAN IS", sample_mean)
    print("")

    sample_stdev = statistics.stdev(meanlist)
    print("THE SAMPLE STDEV IS", sample_stdev)
    print("")

    fig = ff.create_distplot([meanlist], ["Reading Time of each article"], show_hist = False)
    #fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0,1.5], mode = "lines", name = "Mean"))
    fig.show()


def setup():

    master_list = []

    for i in range(0, 100):
        mean = RandomSetOfMeans(30)
        master_list.append(mean)

    drawGraph(master_list)


setup()
    
print("")