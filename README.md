# 🧠 Clinical AI Assistant

An AI-powered clinical reasoning prototype that transforms unstructured clinical-style input into structured analytical outputs using Large Language Models (LLMs) and a domain-specific retrieval pipeline.

> **Note:** This project is an experimental clinical decision-support prototype. It is not intended to provide definitive medical diagnoses or replace assessment by qualified healthcare professionals.

---

## 🚀 Project Overview

Clinical information can be unstructured, incomplete, and difficult to interpret consistently.

This project explores how AI can transform free-text clinical-style input into a structured reasoning workflow.

The current system combines:

* LLM-based clinical reasoning
* Structured prompt-based outputs
* Clinical input validation
* Domain-specific clinical knowledge
* Sentence Transformer embeddings
* FAISS-based vector retrieval
* Streamlit interface
* Modular Python architecture
* Error logging

The project was developed as an exploration of AI-assisted clinical reasoning, information retrieval, and human-AI interaction in healthcare-oriented applications.

---

## ✨ Features

### Structured Clinical Reasoning

The system organizes clinical input into structured analytical categories including:

1. Identified Conditions
2. Key Symptoms
3. Possible Causes
4. Suggested Actions
5. Confidence Level

The structured format is designed to make LLM-generated reasoning easier to inspect and interpret.

### Clinical Input Validation

The application checks user input before sending it to the reasoning workflow.

It handles:

* Empty input
* Very short clinical input
* Basic clinical relevance filtering

### Retrieval-Augmented Knowledge Pipeline

A separate RAG retrieval pipeline has been implemented using a domain-specific clinical knowledge base.

The pipeline:

1. Loads the clinical knowledge base
2. Splits the knowledge base into sections
3. Generates vector embeddings
4. Builds a FAISS vector index
5. Embeds the clinical query
6. Retrieves the top relevant knowledge sections

The current retrieval test uses `top_k=3`.

### Domain-Specific Knowledge Base

The knowledge base contains clinical information covering topics such as:

* Pneumonia
* Acute coronary syndrome and myocardial infarction
* Pulmonary embolism
* Pleurisy
* Fever
* Chest pain
* Dyspnea and difficulty breathing
* Fever with chest pain and dyspnea
* Clinical red flags
* Differential diagnosis principles

The knowledge base emphasizes that symptoms alone are insufficient to establish a definitive diagnosis and that potentially serious presentations require appropriate professional evaluation.

### Error Logging

The application includes an error-logging utility that records application errors to `app.log`.

---

## 🧩 System Architecture

```text
                    ┌──────────────────────┐
                    │   Clinical User Input │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Input Validation   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Structured Prompting │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Llama 3.1 / Groq  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Structured Clinical  │
                    │       Output         │
                    └──────────────────────┘


          Separate RAG Retrieval Pipeline
          
                    Clinical Knowledge Base
                              │
                              ▼
                    Document Loader
                              │
                              ▼
                 Sentence Transformer
                    all-MiniLM-L6-v2
                              │
                              ▼
                       Embeddings
                              │
                              ▼
                       FAISS Index
                              │
                              ▼
                    Clinical Query
                              │
                              ▼
                       Top-k Retrieval
```

---

## 🔬 RAG Pipeline

The retrieval component is implemented as a modular pipeline.

### 1. Knowledge Base Loading

The system loads the clinical knowledge base from:

```text
knowledge_base/medical_knowledge.txt
```

### 2. Document Preparation

The knowledge base is divided into individual clinical knowledge sections.

### 3. Embedding Generation

The project uses:

```text
all-MiniLM-L6-v2
```

through Sentence Transformers to convert knowledge sections into numerical vector representations.

### 4. Vector Index

FAISS is used to create an `IndexFlatL2` vector index.

### 5. Query Retrieval

A clinical query is converted into an embedding and searched against the FAISS index.

The retrieval test returns the top 3 relevant knowledge sections together with their vector distance values.

---

## 🧪 Example Clinical Query

### Input

```text
Patient has fever, chest pain and difficulty breathing.
```

### Retrieval

The RAG pipeline can retrieve relevant knowledge sections related to:

* Pneumonia
* Pulmonary embolism
* Acute coronary syndrome / myocardial infarction
* Pleurisy
* Fever
* Chest pain
* Dyspnea

### Structured Reasoning

The LLM reasoning workflow organizes the clinical input into structured categories rather than returning an unstructured chatbot response.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Application Framework

* Streamlit

### LLM / AI

* Groq API
* Llama 3.1

### Retrieval / Embeddings

* Sentence Transformers
* `all-MiniLM-L6-v2`
* FAISS
* NumPy

### Supporting Libraries

* python-dotenv

### Development Tools

* Git
* GitHub
* Visual Studio Code

---

## 📁 Project Structure

```text
clinical-ai-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── reasoning.py
│   ├── prompts.py
│   ├── config.py
│   ├── validation.py
│   └── utils.py
│
├── rag/
│   ├── document_loader.py
│   ├── embeddings.py
│
```
