import requests
import json
import os

def fetch_manifold_markets(limit=100):
    url = "https://api.manifold.markets/v0/markets"
    params = {
        "limit": limit,
        "sort": "last-bet-time"
    }
    
    print(f"Fetching top {limit} markets from Manifold...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        output_dir = "datasets/manifold"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        output_file = os.path.join(output_dir, "top_markets.json")
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
            
        print(f"Saved {len(data)} markets to {output_file}")
        
        # Create README
        readme_content = """# Manifold Markets Data
        
        Contains snapshot of top markets by liquidity.
        
        - **Source**: https://api.manifold.markets
        - **File**: top_markets.json
        - **Count**: 100
        """
        with open(os.path.join(output_dir, "README.md"), "w") as f:
            f.write(readme_content)
            
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_manifold_markets()
