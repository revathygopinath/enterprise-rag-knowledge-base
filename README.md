# Enterprise RAG System (Bedrock + Gemini)

Built a Retrieval-Augmented Generation (RAG) system using:

- Amazon Bedrock Knowledge Base (retrieval)
- Gemini 2.5 Flash (generation)
- Streamlit (UI)

## Features

- Semantic search over company documents
- Accurate answers grounded in retrieved context
- Controlled output using prompt engineering
- Clean UI for user interaction

## Tech Stack

- AWS Bedrock
- OpenSearch Serverless
- Gemini API
- Python (boto3, Streamlit)

## Run

```bash
pip install -r requirements.txt
streamlit run app.py