# News from the Future 🔮📰

A Generative Journalism platform that uses **LLMs** and **Prediction Markets** to write plausible news articles from the future.

## Overview
This project explores the intersection of collective forecasting and generative AI. By taking probability data from **Manifold Markets** and feeding it into a **Multi-Agent LLM System**, we generate realistic news stories that narrate "what happens" if a prediction comes true (or false).

## Key Findings
- **High Consistency**: The system achieves a 4.9/5 consistency score, meaning generated stories accurately reflect the market's resolution criteria.
- **Plausible Narratives**: The "Analyst -> Journalist" agent workflow produces professionally toned articles that sound like real journalism.
- **Engagement**: Transforming abstract probabilities (e.g., "60%") into concrete stories helps users visualize potential futures.

## Setup & Installation

### Prerequisites
- Python 3.10+
- OpenAI API Key (set as `OPENAI_API_KEY` env var)

### Installation
1.  **Clone the repository** (if not already in workspace).
2.  **Install dependencies** using `uv` (recommended) or `pip`:
    ```bash
    uv venv
    source .venv/bin/activate
    uv add openai streamlit pandas requests python-dotenv plotly
    ```

## Usage

### 1. Run the Web App
Interact with the Future News Engine via a beautiful Streamlit interface:
```bash
streamlit run src/app.py
```
- Browse top prediction markets.
- Generate "YES" or "NO" news scenarios on demand.
- View the AI Analyst's breakdown of the market.

### 2. Run the Experiment
Reproduce the research results:
```bash
python src/experiment_runner.py
```
- Fetches top 5 markets.
- Generates articles for both outcomes.
- Evaluates them using an LLM-as-a-Judge.
- Saves results to `results/experiment_outputs.json`.

## Project Structure
- `src/engine.py`: Core logic for the Analyst and Journalist agents.
- `src/app.py`: Streamlit frontend code.
- `src/experiment_runner.py`: Script for batch generation and evaluation.
- `datasets/manifold/`: Contains cached prediction market data.
- `results/`: Stores experiment outputs and evaluation metrics.
- `REPORT.md`: Detailed research report and analysis.

## Credits
- **Data**: Manifold Markets API
- **Models**: OpenAI GPT-4o
