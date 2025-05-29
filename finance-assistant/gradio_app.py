import gradio as gr
from retriever_agent import query_index
from language_agent import summarize_text

def finance_assistant(query):
    docs = query_index(query)
    combined = " ".join(docs)
    summary = summarize_text(combined)
    return summary

iface = gr.Interface(
    fn=finance_assistant,
    inputs="text",
    outputs="text",
    title="Voice-Based Finance Assistant",
    description="Ask financial questions and get smart summaries!"
)

if __name__ == "__main__":
    iface.launch()
