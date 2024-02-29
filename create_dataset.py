import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

num_buildings = 5

# Date range
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

data = {"timestamp": [], "building_id": [], "energy_consumption": []}

for date in date_range:
    for building_id in range(1, num_buildings + 1):
        timestamp = date + timedelta(hours=random.randint(0, 23))
        energy_consumption = np.random.normal(loc=100, scale=20)
        data["timestamp"].append(timestamp)
        data["building_id"].append(building_id)
        data["energy_consumption"].append(max(0, energy_consumption))

df = pd.DataFrame(data)

df.to_csv("energy_consumption_dataset.csv", index=False)
