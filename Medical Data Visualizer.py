import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
data = pd.read_csv('medical_examination.csv')
def determine_over(row):
    bmi = row['weight']/((row['height']/100)**2)
    return bmi > 25

# Add 'overweight' column
vals = []
for idx,row in data.iterrows():
    vals.append(determine_over(row))
    
data['overweight'] = np.array(vals).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
data['cholesterol'] = (data['cholesterol'] > 1).astype(int)
data['gluc'] = (data['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(data,id_vars = ['cardio'],value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['variable','value','cardio']).size().reset_index(name = 'total')
  
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    plt.figure()
    a = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig = a.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    df_heat = data[(data['ap_lo'] <= data['ap_hi']) &
                 (data['height'] >= data['height'].quantile(0.025)) &
                 (data['height'] <= data['height'].quantile(0.975)) &
                 (data['weight'] >= data['weight'].quantile(0.025)) &
                 (data['weight'] <= data['weight'].quantile(0.975))
                 ]
    

    # Calculate the correlation matrix

    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    sns.heatmap(corr, mask = mask, annot=True,square = True, fmt=".1f", ax = ax)



  # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
    
