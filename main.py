import pandas as pd
import numpy as np
import time
from datetime import datetime
import logging

def generate_synthetic_data():
    seed_value = int(datetime.now().timestamp() * 1000) % (2**32)
    logging.info(f"Random seed used: {seed_value}")
    np.random.seed(seed_value)
    data = {
        'Candidate_ID': range(1, 101),
        'Years_Experience': np.random.randint(0, 20, size=100),
        'Num_Skills': np.random.randint(5, 50, size=100),
        'Education_Level': np.random.choice(['High School', 'Bachelor', 'Masters', 'PhD'], size=100),
        'Interviews_Received': np.random.poisson(lam=3, size=100)
    }
    return pd.DataFrame(data)

def save_data_to_csv(df, filepath):
    """Save DataFrame to a CSV file."""
    df.to_csv(filepath, index=False)

def load_data_from_csv(filepath):
    """Load data from a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def display_data(df):
    """Print the first few rows of the DataFrame."""
    print(df.head())

if __name__ == "__main__":
    # Generate data
    dataframe = generate_synthetic_data()

    # Define the filepath for saving and loading the data
    filepath = 'synthetic_resume_data.csv'

    # Save the data to a CSV file
    save_data_to_csv(dataframe, filepath)

    # Load the data from the CSV file
    loaded_dataframe = load_data_from_csv(filepath)

    # Display the first few rows of the loaded data
    display_data(loaded_dataframe)
