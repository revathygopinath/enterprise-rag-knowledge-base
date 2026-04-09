import os
import boto3
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ── Config ─────────────────────────────────────
AWS_REGION = os.getenv("AWS_REGION")
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

# ── Streamlit UI ───────────────────────────────
st.set_page_config(page_title="Enterprise RAG Chat", page_icon="💬")
st.title("💬 Enterprise Knowledge Base Assistant")

st.markdown("Ask questions based on your company documents.")

# Input
question = st.text_input("🔍 Enter your question")

# ── Ask Button ────────────────────────────────
if st.button("Ask"):

    if not KNOWLEDGE_BASE_ID:
        st.error("Missing KNOWLEDGE_BASE_ID in .env")
    elif not GEMINI_API_KEY:
        st.error("Missing GEMINI_API_KEY in .env")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Thinking..."):

            # ── Step 1: Retrieve from Bedrock ───────────────────
            bedrock = boto3.client(
                "bedrock-agent-runtime",
                region_name=AWS_REGION
            )

            kb_response = bedrock.retrieve(
                knowledgeBaseId=KNOWLEDGE_BASE_ID,
                retrievalQuery={"text": question},
                retrievalConfiguration={
                    "vectorSearchConfiguration": {
                        "numberOfResults": 5
                    }
                },
            )

            # Extract context
            chunks = []
            for item in kb_response.get("retrievalResults", []):
                text = item.get("content", {}).get("text", "")
                if text:
                    chunks.append(text)

            context = "\n\n".join(chunks)

            # Handle no results
            if not context:
                st.warning("No relevant data found in Knowledge Base.")
                st.stop()

            # ── Step 2: Prompt Engineering ──────────────────────
            prompt = f"""
You are an AI assistant answering strictly from company policy documents.

Rules:
- Use ONLY the provided context
- Do NOT modify numbers or percentages
- Do NOT hallucinate
- If answer not found, say "Not available in document"
- Prefer bullet points

Context:
{context}

Question:
{question}
"""

            # ── Step 3: Generate with Gemini ───────────────────
            client = genai.Client()

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            # ── Output ─────────────────────────────────────────
            st.markdown("### 💡 Answer")
            st.write(response.text)

            # Optional: Show sources
            st.markdown("### 📄 Sources")

            for i, chunk in enumerate(chunks):
                    st.markdown(f"**Source {i+1}:**")
                    st.write(chunk[:300] + "...")