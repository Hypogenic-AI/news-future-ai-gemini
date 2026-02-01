import streamlit as st
import engine
import json
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="News from the Future", layout="wide")

st.title("📰 News from the Future")
st.markdown("Generative Journalism powered by Prediction Markets and LLMs.")

# Load Data
@st.cache_data
def load_data():
    try:
        return engine.load_markets()
    except Exception as e:
        st.error(f"Error loading markets: {e}")
        return []

markets = load_data()

if not markets:
    st.warning("No market data found. Please ensure 'datasets/manifold/top_markets.json' exists.")
    st.stop()

# Sidebar
market_questions = [m["question"] for m in markets]
selected_question = st.sidebar.selectbox("Select a Market", market_questions)

# Find selected market
market = next((m for m in markets if m["question"] == selected_question), None)

if market:
    # Market Info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Probability", f"{market.get('probability', 0):.1%}")
    with col2:
        close_ts = market.get('closeTime')
        close_date = datetime.fromtimestamp(close_ts/1000).strftime('%Y-%m-%d') if close_ts else "Unknown"
        st.metric("Resolves By", close_date)
    with col3:
        st.metric("Volume", f"${market.get('volume', 0):,.0f}")

    with st.expander("Market Details"):
        st.write(market.get("textDescription") or market.get("description"))

    # Analysis Section
    st.subheader("1. AI Analyst")
    if "analysis" not in st.session_state or st.session_state.current_market != market['id']:
        st.session_state.current_market = market['id']
        st.session_state.analysis = None
        st.session_state.news_yes = None
        st.session_state.news_no = None

    if st.button("Analyze Market Context"):
        with st.spinner("Analyzing market implications..."):
            analysis_json = engine.analyze_market(market)
            st.session_state.analysis = analysis_json

    if st.session_state.analysis:
        try:
            analysis_dict = json.loads(st.session_state.analysis)
            st.json(analysis_dict)
        except:
            st.text(st.session_state.analysis)

        # Generation Section
        st.subheader("2. Generate Future News")
        
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            st.markdown("### Scenario: YES")
            if st.button("Generate YES Article", key="btn_yes"):
                with st.spinner("Writing article..."):
                    news = engine.generate_news(market, "YES", st.session_state.analysis)
                    st.session_state.news_yes = news
            
            if st.session_state.news_yes:
                st.markdown(st.session_state.news_yes)

        with col_no:
            st.markdown("### Scenario: NO")
            if st.button("Generate NO Article", key="btn_no"):
                with st.spinner("Writing article..."):
                    news = engine.generate_news(market, "NO", st.session_state.analysis)
                    st.session_state.news_no = news
            
            if st.session_state.news_no:
                st.markdown(st.session_state.news_no)

else:
    st.error("Market not found.")
