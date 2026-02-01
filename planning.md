# Research Plan: News from the Future

## Motivation & Novelty Assessment

### Why This Research Matters
Prediction markets aggregate collective wisdom to forecast future events, but their output is typically raw probabilities (e.g., "60% chance X happens"). This data is abstract and dry for the general public. "News from the Future" aims to bridge this gap by converting probabilistic data into concrete, narrative scenarios. This helps decision-makers and the public "feel" the future, making the implications of forecasts more tangible and actionable.

### Gap in Existing Work
Existing research focuses on *improving* forecasts (using LLMs as agents) or *retrieving* information. There is a lack of work on *narrativizing* these forecasts. While "scenario planning" exists, it is often manual. Automated, data-driven narrative generation grounded in real-time market probabilities is a novel intersection of GenAI and Crowd Forecasting.

### Our Novel Contribution
We propose a system that uses LLMs to "collapse the wave function" of prediction markets. We treat a market's probability not just as a number, but as a seed for a generated world state. We will build a prototype "News from the Future" website that presents these generated stories as if they have already happened, grounded in the specific details (resolution criteria) of the markets.

### Experiment Justification
- **Experiment 1 (Pipeline Validation)**: We must verify that LLMs can accurately parse market resolution criteria to generate consistent stories (e.g., if the market is "Will Trump win?", the story shouldn't say he lost *and* won).
- **Experiment 2 (Prototype Deployment)**: The user requested a website. Building a Streamlit app allows us to test the "User Experience" of future news—is it engaging? Is it confusing?

## Research Question
Can Large Language Models, grounded in prediction market data, generate plausible and consistent news articles that narrate future events as if they have already occurred?

## Background and Motivation
Prediction markets are powerful but inaccessible. Stories are the native format of human cognition. We combine the truth-seeking of markets with the storytelling of LLMs.

## Hypothesis Decomposition
1.  **Grounding**: LLMs can extract key entities and resolution criteria from market metadata.
2.  **Coherence**: LLMs can generate a news article that is internally consistent with the market's "YES" or "NO" outcome.
3.  **Plausibility**: The generated news is indistinguishable in tone/style from real news (though the content is fictional).

## Proposed Methodology

### Approach
We will implement a "Future News Engine" using a Multi-Agent LLM workflow:
1.  **Fetcher**: Pulls live data from Manifold Markets (using `datasets/manifold/top_markets.json`).
2.  **Analyst**: Parses the market description and resolution criteria to extract "World Facts".
3.  **Journalist**: Writes a news article based on those World Facts, assuming a specific outcome (e.g., "YES").
4.  **Frontend**: A Streamlit web application to display these headlines and articles.

### Experimental Steps
1.  **Setup**: Initialize `uv` environment and dependencies.
2.  **Data Ingestion**: Verify `top_markets.json` is populated.
3.  **Engine Implementation**: Write `src/engine.py` with `generate_news(market_data, outcome)`.
4.  **Web App**: Build `src/app.py` using Streamlit.
5.  **Evaluation**: Generate 20 stories (10 YES, 10 NO) and evaluate for coherence.

### Baselines
- **Zero-shot Generation**: Ask the LLM to "write a story about X" without the specific market resolution details.
- **Comparison**: Does adding the specific market metadata (resolution criteria) improve the specificity and grounding of the story?

### Evaluation Metrics
- **Consistency Score (1-5)**: Does the story contradict the market outcome? (LLM-as-Judge).
- **Specificity Score (1-5)**: Does the story use specific details from the market description? (LLM-as-Judge).

### Statistical Analysis Plan
- Calculate mean/std for Consistency and Specificity scores.
- T-test comparing Zero-shot vs. Market-Grounded generation.

## Expected Outcomes
We expect the Market-Grounded approach to produce significantly more specific and consistent stories than generic zero-shot prompting.

## Timeline and Milestones
- **Phase 2 (Setup)**: 15 min. Install `streamlit`, `openai`, `requests`, `pandas`.
- **Phase 3 (Implementation)**: 60 min. Build engine and app.
- **Phase 4 (Experiment)**: 30 min. Run generation batch.
- **Phase 5 (Analysis)**: 30 min. Evaluate results.
- **Phase 6 (Docs)**: 20 min. Write Report.

## Potential Challenges
- **Token Limits**: Market descriptions can be long. We may need to summarize.
- **Hallucination**: The LLM might invent facts that contradict the market. The "Analyst" step is designed to mitigate this.

## Success Criteria
- A functional Streamlit app running locally.
- A generated report showing >4/5 average Consistency Score.
