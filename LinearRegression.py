import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(filepath):
    """Load data from a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def plot_scatter(df, feature, target='Interviews_Received'):
    """Plot scatter plots for the specified feature against the target and fit a line of best fit."""
    plt.figure()  # Open a new figure window
    sns.scatterplot(data=df, x=feature, y=target, alpha=0.6, color='blue')
    
    # Fit a line of best fit
    if df[feature].dtype in ['float64', 'int64']:  # Check if the feature is numeric
        m, b = np.polyfit(df[feature], df[target], 1)  # m is slope, b is intercept
        plt.plot(df[feature], m * df[feature] + b, color="red")  # Plot the line of best fit
    
    plt.title(f'Relationship between {feature} and {target}')
    plt.xlabel(feature)
    plt.ylabel(target)
    # Do not call plt.show() here

def plot_education_level(df):
    """Plot a bar graph of the average number of interviews received for each education level."""
    plt.figure(figsize=(8, 6))  # Open a new figure window
    avg_interviews = df.groupby('Education_Level')['Interviews_Received'].mean()
    sns.barplot(x=avg_interviews.index, y=avg_interviews.values, palette="Blues_d")
    
    plt.title('Average Number of Interviews Received by Education Level')
    plt.xlabel('Education Level')
    plt.ylabel('Average Interviews Received')
    plt.xticks(rotation=45)  # Rotate labels to fit long names
    # Do not call plt.show() here

if __name__ == "__main__":
    # Load the data
    data = load_data('synthetic_resume_data.csv')

    # Visualize relationships with scatter plots and lines of best fit
    plot_scatter(data, 'Years_Experience')
    plot_scatter(data, 'Num_Skills')

    # Visualize average interviews received by education level
    plot_education_level(data)

    # Display all plots simultaneously
    plt.show()
