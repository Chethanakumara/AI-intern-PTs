from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def generate_rag_feedback(metrics):
    db = load_vector_store()

    query = (
        f"The code has {metrics['total_lines']} lines, "
        f"{metrics['functions']} functions and "
        f"{metrics['classes']} classes."
    )

    docs = db.similarity_search(query, k=3)
    return [doc.page_content for doc in docs]
