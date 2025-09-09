# Running the project

python3.11 -m venv myenv

source myenv/bin/activate

pip install requests beautifulsoup4 langchain langchain-openai faiss-cpu numpy lxml openai

pip install --upgrade pip

pip install -r requirements.txt

Vector DB Demo (FAISS & Pinecone)

A small project demonstrating how to build embeddings, run local ANN search with FAISS, and store/query vectors in Pinecone.

--------------------------------------------------------------------------------

Prerequisites
- Python 3.11
- macOS/Linux/WSL or Windows (PowerShell equivalents for commands)
- A Pinecone API key (create one at app.pinecone.io)

--------------------------------------------------------------------------------

1) Create & Activate Virtual Environment
  python3.11 -m venv myenv
  source myenv/bin/activate
  # On Windows (PowerShell):
  # .\myenv\Scripts\Activate.ps1

--------------------------------------------------------------------------------

2) Upgrade pip (recommended) & Install Dependencies
  pip install --upgrade pip
  pip install requests beautifulsoup4 langchain langchain-openai faiss-cpu numpy lxml openai
  pip install -r requirements.txt

Note: You can pin versions in a requirements.txt and install with: pip install -r requirements.txt

--------------------------------------------------------------------------------

3) Project Files & Assets
- Typesof_Embeddings.py — examples for text/image/audio embeddings.
  - Ensure the paths are valid for:
    - an image file (e.g., Assets/Panda.jpg)
    - an audio file (e.g., Assets/iPhone_original.mp3) — any audio file is fine
- pinecone_db.py — creates/uses a Pinecone index, upserts vectors, and runs queries.

--------------------------------------------------------------------------------

4) Environment Variables (.env)
Create a .env file at the project root:
  PINECONE_API_KEY=your_pinecone_api_key_here
  # If you use OpenAI in your code, also include:
  # OPENAI_API_KEY=your_openai_api_key_here
The scripts load these via python-dotenv.

--------------------------------------------------------------------------------

5) Run the Examples
  # (venv) run image/text/audio embedding demo
  python Simple_Embedding.py
  python Typesof_Embeddings.py
  
  # (venv) run Fiass example
  python Fiass_db.py
  python Fiass_input_based.py

  # (venv) run Pinecone example
  python pinecone_db.py

--------------------------------------------------------------------------------

6) Pinecone Troubleshooting
If you see errors about deprecated Pinecone plugins (e.g., pinecone-plugin-inference) or package rename conflicts,
clean your environment and reinstall the modern SDK:

  # Inside your active venv
  python -m pip uninstall -y pinecone-client pinecone-plugin-inference pinecone

  # Reinstall ONLY the current SDK and helpers
  python -m pip install "pinecone>=5" sentence-transformers python-dotenv

--------------------------------------------------------------------------------

7) deactivate the Virtual Machine
    
        deactivate

--------------------------------------------------------------------------------

8) Notes
- FAISS is great for fast, local similarity search.
- Pinecone provides a fully managed, scalable vector database with metadata filters and low-latency ANN search.


