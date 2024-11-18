import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #create value to 2050
    years_extended = pd.Series(range(1880, 2051))
    #calculate predictions of sea level
    sea_level_predicted = res.intercept + res.slope * years_extended
    #creating a line
    plt.plot(years_extended, sea_level_predicted, 'r', label="Line of trend #1")
    
    # Create second line of best fit
    #data from 2000
    df_recent = df[df['Year'] >= 2000]
    #line regress for recent data
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    #creating value from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    #calculate predictions for recent data
    sea_levels_recent_predicted = res_recent.intercept + res_recent.slope * years_recent
    #creating 2nd line
    plt.plot(years_recent, sea_levels_recent_predicted, 'g', label="Line of trend #2")

    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()