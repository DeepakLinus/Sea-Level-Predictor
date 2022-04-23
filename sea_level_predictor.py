import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]
    plt.scatter(x,y)

    # Create first line of best fit
    stats=linregress(x,y)
    a=stats.slope
    b=stats.intercept
    x_line=range(1880,2051)
    plt.plot(x_line,a*x_line+b,color="red")
    


    # Create second line of best fit
    df_2000=df[df["Year"]>=2000]
    x=df_2000["Year"]
    y=df_2000["CSIRO Adjusted Sea Level"]
    stats=linregress(x,y)
    a=stats.slope
    b=stats.intercept
    x_line=range(2000,2051)
    plt.plot(x_line,a*x_line+b,color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
