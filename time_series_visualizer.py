import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean the data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

# Function to draw line plot
def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.savefig('line_plot.png')
    plt.show()

# Function to draw bar plot
def draw_bar_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    monthly_avg = df.groupby(['year', 'month'])['value'].mean().unstack()

    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', legend=True)
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.savefig('bar_plot.png')
    plt.show()

# Function to draw box plot
def draw_box_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.savefig('box_plot_year.png')
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='month', y='value', data=df)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.savefig('box_plot_month.png')
    plt.show()

# Call the functions to draw the plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()
