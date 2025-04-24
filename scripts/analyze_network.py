# scripts/analyze_network.py
import os
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Resolve paths
SCRIPT_DIR  = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
data_path   = os.path.join(PROJECT_ROOT, "data", "edges.csv")
results_dir = os.path.join(PROJECT_ROOT, "results")
os.makedirs(results_dir, exist_ok=True)

# Try reading with inferred header
data = pd.read_csv(data_path)

print("Columns found in CSV:", data.columns.tolist())  # diagnostic

# If the columns aren’t what we expect, rename or re-read
if not {'Source','Target'}.issubset(data.columns):
    if set(data.columns) == {0,1}:
        # no header → re-read and assign names
        data = pd.read_csv(
            data_path,
            header=None,
            names=['Source','Target']
        )
    else:
        # maybe lowercase?
        data = data.rename(columns={
            data.columns[0]:"Source",
            data.columns[1]:"Target"
        })

# Build graph
graph = nx.from_pandas_edgelist(data, source='Source', target='Target')

# Draw & save
nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
plt.savefig(os.path.join(results_dir, "network_visualization.png"))
plt.show()
