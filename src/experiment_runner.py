import engine
import json
import os
import pandas as pd
from tqdm import tqdm

def evaluate_article(article, outcome, market_question):
    """
    Evaluator Agent: Scores the article.
    """
    prompt = f"""
    You are an Editor-in-Chief evaluating a draft article.
    
    Market Question: {market_question}
    Intended Outcome: {outcome}
    
    Article Draft:
    {article}
    
    Evaluate on 2 metrics (1-5 scale):
    1. Consistency: Does the article clearly reflect the intended outcome ({outcome}) without contradiction?
    2. Plausibility: Does it sound like a realistic news article (tone, structure, detail)?
    
    Output JSON:
    {{
        "consistency_score": int,
        "consistency_reason": "string",
        "plausibility_score": int,
        "plausibility_reason": "string"
    }}
    """
    
    response = engine.get_llm_response(prompt, system_prompt="You are a critical editor. Output JSON only.")
    clean_response = response.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(clean_response)
    except:
        return {"consistency_score": 0, "plausibility_score": 0, "error": "JSON parse error"}

def run_experiment(num_markets=5):
    markets = engine.load_markets()
    selected_markets = markets[:num_markets]
    
    results = []
    
    print(f"Running experiment on top {num_markets} markets...")
    
    for market in tqdm(selected_markets):
        market_id = market['id']
        question = market['question']
        
        # 1. Analyze
        print(f"\nAnalyzing: {question}")
        analysis_json = engine.analyze_market(market)
        
        # 2. Generate & Evaluate YES
        print("  Generating YES...")
        news_yes = engine.generate_news(market, "YES", analysis_json)
        eval_yes = evaluate_article(news_yes, "YES", question)
        
        results.append({
            "market_id": market_id,
            "question": question,
            "outcome": "YES",
            "article": news_yes,
            "metrics": eval_yes
        })
        
        # 3. Generate & Evaluate NO
        print("  Generating NO...")
        news_no = engine.generate_news(market, "NO", analysis_json)
        eval_no = evaluate_article(news_no, "NO", question)
        
        results.append({
            "market_id": market_id,
            "question": question,
            "outcome": "NO",
            "article": news_no,
            "metrics": eval_no
        })
        
    # Save results
    if not os.path.exists("results"):
        os.makedirs("results")
        
    with open("results/experiment_outputs.json", "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"Saved results to results/experiment_outputs.json")
    
    # Summary Stats
    df = pd.DataFrame([
        {
            "outcome": r["outcome"],
            "consistency": r["metrics"].get("consistency_score", 0),
            "plausibility": r["metrics"].get("plausibility_score", 0)
        }
        for r in results
    ])
    
    print("\nResults Summary:")
    print(df.groupby("outcome").mean())

if __name__ == "__main__":
    run_experiment()
