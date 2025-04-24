# scripts/download_data.py

import pandas as pd

url = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
data = pd.read_csv(url, sep=' ', names=["source", "target"])
data.to_csv("data/edges.csv", index=False)
