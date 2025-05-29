import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from voice_agent import listen, speak
from retriever_agent import query_index
from language_agent import summarize_text

st.set_page_config(page_title="Voice Finance Assistant", page_icon="📊")
st.title("🎤 Voice-Based Finance Assistant")
st.markdown("Speak your query and get a summarized financial insight!")

if st.button("🎙 Speak Now"):
    with st.spinner("🎧 Listening..."):
        query = listen()

    if query:
        st.write(f"📝 You said: **{query}**")
        try:
            docs = query_index(query)
            if docs:
                combined_text = " ".join(docs)
                summary = summarize_text(combined_text)
                st.success(f"📢 Summary:\n{summary}")
                speak(summary)
            else:
                st.warning("⚠️ No relevant documents found.")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("❌ Could not understand your voice. Please try again.")
