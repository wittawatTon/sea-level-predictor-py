import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    #After Year 2000 data
    dfAf2000=df[df['Year']>=2000]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')
    # Create first line of best fit for the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(years_extended, slope * years_extended + intercept, color='yellow', label='Fit: All data')


    # Predict sea level rise for the year 2050
    slopeAf, interceptAf, r_valueAf, p_valueAf, std_errAf = linregress(dfAf2000['Year'], dfAf2000['CSIRO Adjusted Sea Level'])
    years_extendedAf = pd.Series(range(dfAf2000['Year'].min(), 2051))
    plt.plot(years_extendedAf, slopeAf * years_extendedAf + interceptAf, color='red', label='Fit: From 2000')

    yearTarget=2050
    plt.scatter(yearTarget, slopeAf * yearTarget + interceptAf, color='red', s=80, edgecolor='red', zorder=5, label='Point (2025)')
    plt.scatter(yearTarget, slope * yearTarget + intercept, color='yellow', s=80, edgecolor='yellow', zorder=5, label='Point (2025)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
