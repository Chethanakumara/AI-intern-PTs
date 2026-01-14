🚀 Code Analyzer Tool with RAG

A Python-based Code Analyzer that performs static analysis on Python files and provides AI-powered feedback using Retrieval-Augmented Generation (RAG).

This project was built as part of an AI Internship assignment to demonstrate how traditional tools can be enhanced using AI.

🎯 Project Objective (Motive)

The goal of this project is to:

Analyze Python source code

Extract useful metrics like lines, functions, and classes

Improve the tool by integrating RAG to provide intelligent suggestions based on coding best practices

🧠 What is Improved Using RAG?
Before (Without RAG)

Only counted lines, functions, and classes

Output was static and rule-based

After (With RAG)

Retrieves Python best practices from a knowledge base

Uses embeddings + vector search (FAISS)

Provides AI-based suggestions like:

Code readability improvements

Modularization tips

Maintainability suggestions

➡️ This turns the project into a smart code review assistant.

🛠️ Tech Stack

Python

AST (Abstract Syntax Tree)

LangChain

FAISS (Vector Database)

HuggingFace Embeddings

RAG (Retrieval-Augmented Generation)

📁 Project Structure
code-analyzer-rag/
│
├── code_analyzer.py        # Main analyzer (AST-based)
├── rag_engine.py           # RAG logic & AI feedback
├── build_vector_store.py   # Builds FAISS vector database
├── knowledge_base.txt      # Python best practices
├── README.md
├── .gitignore
└── venv/

🔄 Workflow Diagram 
          ┌────────────────────┐
          │  Python Code File  │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │  AST Code Analyzer │
          │ (lines, functions) │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │  Analysis Result   │
          └─────────┬──────────┘
                    │
                    ▼
     ┌─────────────────────────────┐
     │  RAG Engine (LangChain)     │
     │  • Embeddings              │
     │  • FAISS Vector Search     │
     └─────────┬──────────────────┘
               │
               ▼
     ┌─────────────────────────────┐
     │  AI-Based Code Feedback     │
     │  (Best practices & tips)   │
     └─────────────────────────────┘

