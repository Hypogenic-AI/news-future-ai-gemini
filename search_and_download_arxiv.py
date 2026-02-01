import arxiv
import os

def search_and_download(query, max_results=10):
    print(f"Searching for: {query}")
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = list(client.results(search))
    
    if not os.path.exists("papers"):
        os.makedirs("papers")
        
    readme_content = "# Downloaded Papers\n\n"
    if os.path.exists("papers/README.md"):
        with open("papers/README.md", "r") as f:
            readme_content = f.read()

    downloaded_count = 0
    for r in results:
        # Sanitize filename
        safe_id = r.get_short_id().replace("/", "_")
        safe_title = "".join([c if c.isalnum() else "_" for c in r.title])[:50]
        filename = f"{safe_id}_{safe_title}.pdf"
        filepath = os.path.join("papers", filename)
        
        if not os.path.exists(filepath):
            print(f"Downloading: {r.title}")
            try:
                r.download_pdf(dirpath="papers", filename=filename)
                downloaded_count += 1
                
                entry = f"## [{r.title}]({filename})\n"
                entry += f"- **Authors**: {', '.join([a.name for a in r.authors])}\n"
                entry += f"- **Year**: {r.published.year}\n"
                entry += f"- **arXiv**: {r.entry_id}\n"
                entry += f"- **Summary**: {r.summary.replace(chr(10), ' ')}\n\n"
                
                readme_content += entry
            except Exception as e:
                print(f"Failed to download {r.title}: {e}")
    
    with open("papers/README.md", "w") as f:
        f.write(readme_content)
        
    print(f"Downloaded {downloaded_count} new papers.")

if __name__ == "__main__":
    queries = [
        "\"Large Language Models\" prediction markets",
        "\"Large Language Models\" forecasting",
        "\"Large Language Models\" future events",
        "AI agents prediction markets"
    ]
    
    for q in queries:
        search_and_download(q, max_results=3)