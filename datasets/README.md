# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size.

## Dataset 1: Manifold Markets Snapshot

### Overview
- **Source**: [Manifold Markets API](https://api.manifold.markets)
- **File**: `datasets/manifold/top_markets.json`
- **Size**: ~100 markets
- **Format**: JSON
- **Content**: Top 100 markets sorted by `last-bet-time` (active markets).
- **Date Fetched**: 2026-01-31

### Download Instructions

To reproduce this dataset, run the fetch script:
```bash
python fetch_manifold_markets.py
```

### Loading the Dataset

```python
import json
import os

with open("datasets/manifold/top_markets.json", "r") as f:
    markets = json.load(f)

print(f"Loaded {len(markets)} markets")
# Example access
print(markets[0]['question'])
```

### Notes
- The API parameters used were `limit=100` and `sort=last-bet-time`.
- This dataset serves as a seed for "future events" to generate news about.
