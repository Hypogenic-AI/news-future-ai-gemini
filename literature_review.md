# Literature Review: News from the Future

## Research Area Overview
The intersection of Large Language Models (LLMs) and Prediction Markets offers a novel domain for "Generative Journalism" and "Future Forecasting". This review explores how LLMs can be used to generate plausible narratives about future events based on market probabilities, and how they can participate in markets as forecasting agents.

## Key Papers

### 1. Integrating Traditional Technical Analysis with AI: A Multi-Agent LLM-Based Approach to Stock Market Forecasting
- **Relevance**: High. Demonstrates a multi-agent system ("ElliottAgents") for financial forecasting.
- **Key Insight**: LLMs can successfully interpret complex market data (technical analysis patterns) and make predictions. This supports the hypothesis that LLMs can understand market signals.
- **Methodology**: Multi-agent framework (Analysis Agent, Risk Agent, etc.) using RAG.

### 2. Foundations of GenIR (Generative Information Retrieval)
- **Relevance**: High. Discusses "Information Synthesis" and "Information Generation".
- **Key Insight**: Generative AI moves beyond retrieval to synthesizing new, grounded content. This is the core mechanism for "generating news" based on prediction market data (the "grounding" source).

### 3. Unmasking the Shadows of AI: Investigating Deceptive Capabilities in LLMs
- **Relevance**: Medium. Discusses "Strategic Deception".
- **Key Insight**: While focused on safety, the ability of LLMs to generate "deceptive" (or in our case, "fictional but plausible") content is crucial for simulating future news scenarios that haven't happened yet.

### 4. Is Self-knowledge and Action Consistent: Investigating LLM Personality
- **Relevance**: Low/Medium.
- **Key Insight**: Discusses consistency of LLM personas. Relevant for maintaining a consistent "journalist" or "reporter" persona in the news generation system.

## Common Methodologies
- **Multi-Agent Systems**: Using specialized agents for analysis, risk assessment, and content generation (Paper 1).
- **RAG (Retrieval-Augmented Generation)**: Grounding generation in external data (market data, technical indicators) to prevent hallucination (Papers 1, 2).

## Datasets in Literature
- **Financial Data**: Historical stock prices (Paper 1).
- **Prediction Markets**: implied datasets from platforms like Manifold, Polymarket (implied by domain, though not explicitly central in the gathered papers).

## Gaps and Opportunities
- **Narrative Generation from Probabilities**: While papers discuss *forecasting* prices, there is a gap in *narrativizing* these forecasts into news stories.
- **Counterfactual News**: Generating news for events that *might* happen (high probability) vs. those that are unlikely, which is the core of "News from the Future".

## Recommendations for Experiment
1.  **Dataset**: Use **Manifold Markets** data as the "ground truth" for future probabilities. It is rich, accessible, and covers diverse topics beyond finance.
2.  **Methodology**: Adopt a **Multi-Agent** approach (similar to ElliottAgents):
    -   **Analyst Agent**: Interprets market probability (e.g., "60% chance of X").
    -   **Journalist Agent**: Writes the story assuming X happens.
    -   **Editor Agent**: Verifies plausibility and tone.
3.  **Metrics**: Evaluate "Plausibility" (human eval or LLM-as-judge) and "Alignment" (does the story match the market probability?).
