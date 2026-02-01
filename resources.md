# Resources Catalog

## Summary
This document catalogs all resources gathered for the "News from the Future" research project.

### Papers
Total papers downloaded: 6

| Title | Key Info | File |
|-------|----------|------|
| Integrating Traditional Technical Analysis with AI | Multi-Agent Forecasting | `2506.16813v1_...pdf` |
| Foundations of GenIR | Information Synthesis | `2501.02842v1_...pdf` |
| Unmasking the Shadows of AI | Deception/Plausibility | `2403.09676v1_...pdf` |
| Is Self-knowledge and Action Consistent | Personas | `2402.14679v2_...pdf` |
| Large Language Models Lack Understanding... | Tokenization (Low relevance) | `2405.11357v3_...pdf` |
| A cybersecurity AI agent... | Agent Selection | `2510.01751v1_...pdf` |

See `papers/README.md` for details.

### Datasets

| Name | Source | Size | Location |
|------|--------|------|----------|
| Manifold Markets Top 100 | API | 100 mkts | `datasets/manifold/top_markets.json` |

See `datasets/README.md` for details.

### Code Repositories

| Name | Purpose | Location |
|------|---------|----------|
| Metaculus Forecasting Tools | API/Bots | `code/metaculus-forecasting-tools` |
| Polymarket Data | Data Fetching | `code/poly-data` |

See `code/README.md` for details.

### Resource Gathering Notes
- **Strategy**: Used `arxiv` API for papers, Manifold API for data, and GitHub for code.
- **Challenges**: `paper-finder` service was unavailable, requiring a custom script. Manifold API params needed adjustment.
- **Recommendations**: Use Manifold data for the primary experiment as it is the most accessible and diverse. Use the Multi-Agent approach inspired by the "ElliottAgents" paper.
