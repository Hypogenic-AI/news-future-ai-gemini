import json
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI Client
# Note: In this environment, we rely on the environment variable OPENAI_API_KEY
client = openai.OpenAI()

def load_markets(filepath="datasets/manifold/top_markets.json"):
    """Loads markets from the local JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Market data not found at {filepath}")
    
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def get_llm_response(prompt, model="gpt-4o", system_prompt="You are a helpful assistant."):
    """Helper to call OpenAI API."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def analyze_market(market):
    """
    Analyst Agent: Extracts 'World Facts' and context from the market.
    """
    description = market.get("textDescription", "") or market.get("description", "")
    # Clean description if it's JSON-like or too long
    if isinstance(description, dict):
        description = json.dumps(description)
    
    prompt = f"""
    You are an Expert Analyst for a Future News service.
    Your goal is to analyze a prediction market and extract the 'World Facts' that would be true if this market resolves.
    
    Market Question: {market['question']}
    Market Description: {description[:2000]}  # Truncate to avoid huge context
    Resolution Criteria: {market.get('resolution', 'Unknown')}
    
    Output a JSON object with:
    1. 'key_entities': List of people, organizations, or places involved.
    2. 'context': A 1-sentence summary of the status quo.
    3. 'implications_if_yes': What happens if the answer is YES? (2-3 bullet points)
    4. 'implications_if_no': What happens if the answer is NO? (2-3 bullet points)
    """
    
    response = get_llm_response(prompt, model="gpt-4o", system_prompt="You are an expert analyst. Output valid JSON.")
    
    # Simple cleanup to ensure JSON
    response = response.replace("```json", "").replace("```", "").strip()
    return response

def generate_news(market, outcome, analysis_json):
    """
    Journalist Agent: Writes a news article.
    """
    try:
        analysis = json.loads(analysis_json)
    except:
        analysis = {"context": "Unknown", "implications_if_yes": [], "implications_if_no": []}
    
    implications = analysis['implications_if_yes'] if outcome == "YES" else analysis['implications_if_no']
    impl_text = "\n".join([f"- {i}" for i in implications])
    
    prompt = f"""
    You are a Pulitzer-prize winning Journalist reporting from the future.
    
    NEWS ALERT: The event "{market['question']}" has just happened!
    The outcome is: {outcome}.
    
    Context: {analysis.get('context')}
    Key Implications:
    {impl_text}
    
    Write a breaking news article (Headline + Body). 
    - Date: The future (make it realistic based on the market close time: {market.get('closeTime')}).
    - Tone: Professional, objective, but engaging.
    - Structure: Catchy Headline, Dateline, Lead Paragraph (Who, what, when, where, why), Body (Details, quotes from fictional experts), Conclusion.
    - Length: ~300 words.
    
    Make it sound real. Treat the prediction market outcome as a hard fact that just occurred.
    """
    
    return get_llm_response(prompt, model="gpt-4o", system_prompt="You are a journalist reporting on future events.")

if __name__ == "__main__":
    # Test run
    markets = load_markets()
    print(f"Loaded {len(markets)} markets.")
    m = markets[0]
    print(f"Analyzing: {m['question']}")
    analysis = analyze_market(m)
    print("Analysis:", analysis)
    print("Generating YES news...")
    news = generate_news(m, "YES", analysis)
    print("\n" + news)
