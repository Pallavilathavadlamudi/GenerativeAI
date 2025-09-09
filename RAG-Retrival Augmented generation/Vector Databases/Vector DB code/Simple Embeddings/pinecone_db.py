from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os, time

load_dotenv()
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
print("Pinecone initialized successfully.")

model = SentenceTransformer("all-MiniLM-L6-v2")
print("SentenceTransformer model loaded.")

texts = [
    "Pinecone is a vector database.",
    "Vectors represent data in numerical form.",
    "Embedding models convert text to vectors.",
    "Convert data → embeddings (vectors of floats).",
    "Store vectors + metadata in Pinecone index.",
    "Query = embedding → Pinecone finds nearest neighbors.",
    "Uses ANN search (cosine/dot product).",
    "Supports metadata filters + scalable infra.",
    "Use cases: RAG, semantic search, recommendations, anomaly detection.",
]

embeddings = model.encode(texts)
dim = embeddings.shape[1]
print(f"Converted {len(texts)} texts to embeddings.\nVector dimension: {dim}")

index_name = "exampleindex"

# Ensure we compare against names
existing = {ix.name for ix in pc.list_indexes()}
if index_name not in existing:
    pc.create_index(
        name=index_name,
        dimension=dim,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print(f"Created new index: {index_name}")

# Wait until the index is READY before upsert/query
while True:
    ix = next(i for i in pc.list_indexes() if i.name == index_name)
    if getattr(ix, "status", None) and getattr(ix.status, "ready", False):
        break
    print("Waiting for index to be ready...")
    time.sleep(2)

index = pc.Index(index_name)
print(f"Connected to index: {index_name}")

# Upsert
vectors = [(str(i), embeddings[i].tolist(), {"text": texts[i]}) for i in range(len(texts))]
index.upsert(vectors=vectors)
print(f"Inserted {len(vectors)} vectors into the index.")

# Optional: verify we actually have vectors
stats = index.describe_index_stats()
print("Index stats:", stats)

# Query
query_text = "Is pinecone vector database?"
query_vec = model.encode([query_text])[0].tolist()
print(f"Encoded query: '{query_text}'")

result = index.query(vector=query_vec, top_k=3, include_metadata=True)

if getattr(result, "matches", []):
    print("\nQuery Results:")
    for m in result.matches:
        print(f"ID: {m.id}  Score: {m.score:.4f}")
        print(f"Text: {m.metadata.get('text','')}\n")
else:
    print("No matches found.")
