# rag-pipeline
┌──────────────────────────────┐
│ 1. User Question Input       │
│------------------------------│
│ What happens:               │
│ User submits a question     │
│                              │
│ Tech: Frontend / API / CLI   │
│ Data: Raw text query         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 2. Query Embedding           │
│------------------------------│
│ What happens:               │
│ Convert question → vector    │
│ representation               │
│                              │
│ Tech: Embedding model        │
│ (OpenAI / sentence-transformers)
│ Data: Dense vector           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 3. Vector DB Retrieval       │
│------------------------------│
│ What happens:               │
│ Find most similar chunks     │
│ using cosine similarity      │
│                              │
│ Tech: FAISS / Pinecone /     │
│ ChromaDB                     │
│ Data: Top-k document chunks  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 4. Prompt Assembly           │
│------------------------------│
│ What happens:               │
│ Combine:                    │
│ - system instructions       │
│ - retrieved context chunks  │
│ - user question             │
│                              │
│ Tech: Python prompt builder  │
│ Data: Structured prompt text │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ 5. LLM Generation            │
│------------------------------│
│ What happens:               │
│ Model generates answer using │
│ context + instructions       │
│                              │
│ Tech: GPT / LLM API          │
│ Data: Final response text    │
└──────────────────────────────┘
