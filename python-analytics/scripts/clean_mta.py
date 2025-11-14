# clean_mta.py
# Script to batch clean raw MTA CSVs

import pandas as pd
import os

raw_folder = '../data/raw/'
processed_folder = '../data/processed/'

for file in os.listdir(raw_folder):
    if file.endswith('.csv'):
        df = pd.read_csv(os.path.join(raw_folder, file))
        df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
        df.to_json(os.path.join(processed_folder, file.replace('.csv', '.json')))
        print(f"Processed {file}")

