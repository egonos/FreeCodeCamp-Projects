import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    def y_hat(x):
        model = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
        x = x.values
        xx = np.array([*range(2014,2051)])
        x = np.concatenate([x,xx],axis = 0)
        return x,x*model.slope+ model.intercept
    
    def y_hat_sec(x):
        x = x.values
        mask = x>=2000
        x = x[mask]
        model = linregress(x,df['CSIRO Adjusted Sea Level'].values[mask])
        xx = np.array([*range(2014,2051)])
        x = np.concatenate([x,xx],axis = 0)
        return x, model.slope*x+model.intercept

    fig,ax = plt.subplots()

    df[['Year','CSIRO Adjusted Sea Level']].plot(kind = 'scatter', x = 'Year',y = 'CSIRO Adjusted Sea Level',ax = ax)
    x,y = y_hat(df['Year'])
    ax.plot(x,y)
    x,y = y_hat_sec(df['Year'])
    ax.plot(x,y)
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()