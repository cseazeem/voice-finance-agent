from transformers import pipeline
from typing import List

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)

def summarize_text(text: str) -> str:
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]["summary_text"]

def summarize_chunks(chunks: List[str]) -> str:
    combined = " ".join(chunks)
    return summarize_text(combined)
