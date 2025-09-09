import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

try:
    # Load a pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("SentenceTransformer model loaded.")

    # Sample custom data (text)
    texts = [
        "FAISS is a library for efficient similarity search.",
        "Vectors represent data in numerical form.",
        "Embedding models convert text to vectors.",
        "Local vector databases can be faster for small datasets.",
        "FAISS supports both CPU and GPU operations."
    ]

    # Convert texts to vectors
    embeddings = model.encode(texts)
    print(f"Converted {len(texts)} texts to embeddings.")

    # Define vector dimension based on the model's output
    dimension = embeddings.shape[1]
    print(f"Vector dimension: {dimension}")

    # Create a FAISS index
    index = faiss.IndexFlatL2(dimension)
    
    # Add vectors to the index
    index.add(embeddings)
    print(f"Created FAISS index and added {len(embeddings)} vectors.")

    # Example query
    query_text = "What is FAISS?"
    query_vector = model.encode([query_text])[0]
    print(f"Encoded query: '{query_text}'")

    # Perform the query
    k = 3  # number of nearest neighbors to retrieve
    distances, indices = index.search(np.array([query_vector]), k)

    # Process and print results
    print("\nQuery Results:")
    for i in range(len(indices[0])):
        print(f"Rank: {i+1}")
        print(f"Text: {texts[indices[0][i]]}")
        print(f"Distance: {distances[0][i]}")
        print()

except Exception as e:
    print(f"An error occurred: {e}")


    '''1. The script first imports three libraries:
            NumPy for handling arrays
            FAISS for fast similarity search
            SentenceTransformer for converting text into numerical embeddings
            
            numpy: Used to manipulate arrays (vectors)
            faiss: Fast Approximate Nearest Neighbor Search (used for indexing and searching)
            SentenceTransformer: Converts text into embeddings (vectors)
        
        2. It then loads a pre-trained sentence embedding model called all-MiniLM-L6-v2. This model converts text into 384-dimensional vectors that capture semantic meaning.

            Loads the all-MiniLM-L6-v2 model
            This model transforms text into 384-dimensional vectors
            It's a lightweight, fast model great for semantic similarity

        3. A list of five text sentences is defined. These sentences are related to FAISS, embeddings, and vectors.

        4. Each of these texts is passed through the embedding model to generate numerical vectors. At this stage, each sentence is represented as a dense vector of size 384.

            Transforms each sentence into a dense vector
            Shape: [5, 384] (5 sentences, each 384-dim)

        5. The script creates a FAISS index. Since the embeddings are 384-dimensional, the index is initialized with this dimension. The index type used is IndexFlatL2, which performs similarity search using Euclidean (L2) distance.

            IndexFlatL2: Creates a brute-force FAISS index using L2 (Euclidean) distance
            dimension: Must match the vector size (384 here)

        6. All of the sentence embeddings are then added to the FAISS index. This prepares the index for searching.

            Adds all 5 vectors to the FAISS index
            Now the index is ready to be searched!

        7. A query sentence — “What is FAISS?” — is encoded into a 384-dimensional vector using the same embedding model.

            You encode the query into a vector (same 384-dim space)
            encode() returns a batch, so [0] extracts the first vector

        8. The query vector is then searched against the index. The script asks FAISS to return the three closest matches (top-3 nearest neighbors). FAISS compares the query vector with each stored vector and returns the closest ones based on distance.

            search() finds the k=3 closest vectors in the index to the query
            Returns:
            indices: The indexes of the closest texts
            distances: Corresponding L2 distances (smaller = more similar)

        9. Finally, the script prints out the results. For each of the top-3 matches, it shows:
            The rank (1st, 2nd, 3rd)
            The text from the original list that was closest in meaning
            The distance score (smaller numbers mean closer similarity)
            
            Outputs the top 3 most similar texts to "What is FAISS?" based on the vector space'''