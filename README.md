# 🧠 Enterprise Knowledge Base Q&A System (Hybrid RAG)

## 🚀 Overview

This project is an **Enterprise-grade Knowledge Base Question Answering System** built using a **Hybrid Retrieval-Augmented Generation (RAG)** architecture.

It allows users to query internal company documents and receive **accurate, context-aware answers with source citations**, reducing hallucinations and improving trust in responses.

---

## 🏗️ Architecture

```
User Query → Streamlit UI → Amazon Bedrock (Retrieve)
           → OpenSearch Serverless (Vector Store)
           → Context Retrieved → Gemini 2.5 Flash (LLM)
           → Final Answer + Citations
```

---

## ✨ Key Features

* 🔍 Context-aware question answering
* 📚 Citation-based responses (source transparency)
* 🚫 Reduced hallucination using grounded retrieval
* ⚡ Hybrid RAG (Bedrock + external LLM)
* 🖥️ Clean and interactive Streamlit UI
* 🔐 Secure IAM Role-based authentication (no hardcoded credentials)

---

## 🧰 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Cloud Services:**

  * Amazon Bedrock (Knowledge Base & Retrieval)
  * OpenSearch Serverless (Vector Database)
  * Amazon S3 (Document Storage)
* **LLM:** Gemini 2.5 Flash
* **SDK:** Boto3

---

## 📸 Demo (Add after deployment)

### UI

*Add screenshot here*

### Answer with Citations

*Add screenshot here*

---

## ⚙️ Local Setup

```bash
git clone https://github.com/revathygopinath/enterprise-rag-knowledge-base.git
cd enterprise-rag-knowledge-base

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## ☁️ Deployment (AWS EC2)

* Deployed on AWS EC2 instance
* Configured inbound rule for port **8501**
* IAM Role attached to EC2 for secure access:

  * Amazon Bedrock
  * Amazon S3
  * OpenSearch Serverless
* No AWS access keys used

---

## 🔐 Security Best Practices

* ❌ No hardcoded credentials
* ❌ `.env` not pushed to repository
* ✅ IAM Role-based authentication used
* ✅ Principle of least privilege (can be refined)

---

## 📂 Project Structure

```
enterprise-rag-knowledge-base/
├── app.py                # Main Streamlit app
├── app_gemini.py        # Gemini integration
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

---

## 🚀 Future Enhancements

* 🐳 Docker containerization
* 🔁 CI/CD pipeline (GitHub Actions)
* 🌐 Custom domain + HTTPS
* 👥 Role-based access control (RBAC)
* 📊 Logging and monitoring

---

## 💼 Resume Highlights

* Built and deployed a **Hybrid RAG system** using Amazon Bedrock and OpenSearch
* Implemented **citation-based QA system** to reduce hallucination
* Designed secure cloud architecture using **IAM role-based authentication**
* Developed interactive frontend using **Streamlit**

---

## 👨‍💻 Author

**Revathy Gopinath**
