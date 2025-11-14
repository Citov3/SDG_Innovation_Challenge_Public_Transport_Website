# merge_sources.py
# Merge MTA + Traffic datasets into a single file

import pandas as pd
import json

mta = pd.read_json('../data/processed/mta_penn_hourly.json')
traffic = pd.read_json('../data/processed/traffic_hourly.json')

merged = mta.join(traffic, how='outer')
merged.fillna(0, inplace=True)

merged.to_json('../data/processed/merged_data.json')
print("Merged MTA and traffic data saved!")
