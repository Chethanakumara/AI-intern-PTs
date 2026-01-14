from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load knowledge base
with open("knowledge_base/python_best_practices.txt", "r") as file:
    texts = file.readlines()

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Build FAISS vector store
vector_store = FAISS.from_texts(texts, embeddings)

# Save FAISS index
vector_store.save_local("faiss_index")

print("✅ FAISS vector store created successfully")
