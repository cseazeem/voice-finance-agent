from agents.retriever_agent import query_index
from agents.language_agent import summarize_chunks

if __name__ == "__main__":
    chunks = query_index("Asia tech stock performance")
    summary = summarize_chunks(chunks)
    print("📢 Summary:")
    print(summary)
