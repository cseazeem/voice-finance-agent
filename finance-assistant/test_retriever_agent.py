from agents.retriever_agent import build_faiss_index, query_index

if __name__ == "__main__":
    # Step 1: Build FAISS index from sample file
    build_faiss_index("sample_market_news.txt")

    # Step 2: Run a test query
    result = query_index("Asia tech stock performance")
    for i, chunk in enumerate(result):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("-" * 40)
