# 📚 RAG-Based Chatbot with Free Hugging Face API

This repository contains a **Retrieval-Augmented Generation (RAG) chatbot** built using **Python, LangChain, FAISS, and a free Hugging Face model**. It can **ingest PDFs**, extract relevant information, and generate responses **without relying on OpenAI's paid API**.

## 🚀 Features
- **PDF Processing:** Extracts and splits text into manageable chunks.
- **Vector Search with FAISS:** Stores and retrieves relevant text using embeddings.
- **Free Hugging Face Model:** Uses `mistralai/Mistral-7B-v0.1` for response generation.
- **End-to-End RAG Pipeline:** Retrieves contextually relevant answers based on queries.
- **Completely Free API Usage!**


## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/chatbot_project.git
cd chatbot_project
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Download a Free Hugging Face Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

### 4️⃣ Run the Chatbot
```python
python test.py
```

---

## 📌 How It Works
### 📝 1. Load & Process a PDF
- Extracts **text** from the PDF.
- Splits text into **overlapping chunks**.

### 🏗️ 2. Convert Text into Embeddings
- Uses **FAISS** for efficient vector search.
- Stores chunk embeddings for **fast retrieval**.

### 🤖 3. Answer Queries
- Retrieves **relevant document sections**.
- Uses a **free Hugging Face model** to generate answers.

---

## 📬 Contact & Contributions
- Feel free to **fork** this repo and contribute!
- If you find issues, **open a GitHub issue**.
- Connect on **LinkedIn**: [Tarek Ashraf]([https://linkedin.com/in/your-profile](https://www.linkedin.com/in/tarek-ashraf-393632193/))

Happy coding! 🎯


 
