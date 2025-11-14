# utils/mta_utils.py
# Helper functions for MTA data formatting + cleaning

import pandas as pd

def clean_mta_times(df):
    """
    Converts 'time' column into datetime objects.
    Ensures the dataset is uniform for analysis.
    """
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
    return df


def group_station_busy(df, station_name):
    """
    Filters dataset for a single station and summarizes busy levels.
    Equivalent to your Python code in Colab.
    """
    station_df = df[df['Station'] == station_name]
    station_df = clean_mta_times(station_df)
    
    grouped = station_df.groupby('time').agg({'busy': 'sum'})
    grouped = grouped.resample('60T').sum().sort_values(by='busy', ascending=False)
    return grouped
