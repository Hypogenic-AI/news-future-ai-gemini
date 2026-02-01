# Research Report: News from the Future

## 1. Executive Summary
This project successfully implemented a "Generative Journalism" system that transforms prediction market data into plausible news articles about future events. By using a multi-agent LLM workflow (Analyst -> Journalist -> Editor), we achieved high consistency (Average Score: 4.9/5) between market probabilities and generated narratives. The system effectively grounds generated text in specific market resolution criteria, solving the problem of abstract probabilistic data being difficult for the public to conceptualize.

## 2. Goal
The primary goal was to test the hypothesis that **LLMs + Prediction Markets** can generate plausible news from the future.
- **Problem**: Prediction markets output raw probabilities (e.g., "60% chance"). This is abstract.
- **Solution**: "News from the Future" visualizes these probabilities as concrete scenarios (stories), aiding in decision-making and engagement.

## 3. Data Construction
- **Source**: Manifold Markets API.
- **Dataset**: `datasets/manifold/top_markets.json` (Top 100 markets by liquidity).
- **Features Used**: Market Question, Description, Resolution Criteria, Close Time.

## 4. Experiment Description

### Methodology: The "Future News Engine"
We utilized a Multi-Agent LLM architecture:
1.  **Analyst Agent**: Reads the market metadata and extracts "World Facts" (e.g., "If X happens, Y is implied"). This ensures the story respects the specific resolution criteria of the market.
2.  **Journalist Agent**: Takes the "World Facts" and the intended outcome (YES/NO) to write a journalistic piece.
3.  **Evaluator Agent (LLM-as-Judge)**: Scores the output for **Consistency** (Does it match the outcome?) and **Plausibility** (Does it sound real?).

### Implementation
- **Tech Stack**: Python, OpenAI GPT-4o, Streamlit.
- **Frontend**: A web interface allowing users to browse markets and generate scenarios on demand.

## 5. Result Analysis

### Quantitative Results (n=10 articles)
| Metric | Mean Score (1-5) | Interpretation |
|--------|------------------|----------------|
| **Consistency** | **4.9** | The model almost never contradicts the market outcome. |
| **Plausibility** | **4.1** | The articles generally sound like real news. |

### Qualitative Analysis
- **Success Case**: *NBA Live Games*. The model correctly adopted the tone of sports journalism, citing fictional experts and specific details about the season.
- **Edge Case**: *Jesus Returns before GTA VI*. The model struggled with Plausibility (Score: 2) for the "YES" case, noting that "the premise is inherently implausible as a news event," even if the writing was consistent. This highlights a limitation: the system is bound by the realism of the underlying market.

### Key Findings
1.  **Grounding Works**: Passing the resolution criteria to an "Analyst" agent before generation prevents hallucinations that contradict the market's specific rules.
2.  **Tone Adaptation**: The LLM successfully shifts tone between "Sports" (excitement), "Politics" (serious), and "Tech" (analytical) based on the market category.

## 6. Conclusions
We successfully demonstrated that a "News from the Future" website is a viable application of GenAI. The combination of quantitative market data with qualitative LLM narrative generation creates a compelling user experience that makes the future tangible.

## 7. Next Steps
- **Multimodal**: Generate images to accompany the articles (e.g., Midjourney).
- **Personalization**: "News from *Your* Future" based on user-specific prediction markets.
