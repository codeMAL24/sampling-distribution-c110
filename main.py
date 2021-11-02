import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
mean = s.mean(data)
std = s.stdev(data)

print(f"Population mean : {mean}")
print(f"Population SD : {std}")


# mean = s.mean(dataSet)
# std = s.stdev(data)

# # print(f"Mean sample data : {mean}")
# # print(f"STD of sample data: {std}")    

def showFig(meanList):
    df = meanList
    mean = s.mean(df)
    fig = ff.create_distplot([df],["temperature"], show_hist=False)
    fig.show()

def rsom(counter):
    #rsom = random set of means
    dataSet = []
    for i in range(0,counter):
        r = random.randint(0,len(data)-1)
        value = data[r]
        dataSet.append(value)
    mean = s.mean(dataSet)
    return mean

def setup():
    mlist = []
    for i in range(0,1000):
        som = rsom(100)
        mlist.append(som)
    showFig(mlist)
    m = s.mean(mlist)
    print(f"mean of sampling distribution{m}")    
    std = s.stdev(mlist)
    print(f"std of sampling distribution{std}") 
setup()  
#mean of sample and mean of population is equal
#SD of the sampling mean =  SD Population / sqrt (number of data in each sample)
# sd of sample mean = 5.699 / 10
# sd of sample mean = 0.5699