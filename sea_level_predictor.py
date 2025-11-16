import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    df = pd.read_csv('epa-sea-level.csv')

    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, intercept1 + slope1 * pd.Series(years_extended), 'r')

    
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = range(2000, 2051)
    plt.plot(years_recent_extended, intercept2 + slope2 * pd.Series(years_recent_extended), 'green')

    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
