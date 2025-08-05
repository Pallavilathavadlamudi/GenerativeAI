## **NLP– Introduction to Natural Language Processing**

### What is NLP?

**Natural Language Processing (NLP)** is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and human language. It allows machines to read, understand, interpret, and even generate human languages (like English, Spanish, etc.).

It combines:

* **Linguistics**: Study of language structure.
* **Machine Learning**: Learning from data (text/speech).
* **Computer Science**: Algorithms and processing power.

**Example use cases**:

* Siri/Alexa understanding commands
* Google Translate
* Chatbots like ChatGPT

---

## NLP in the Context of AI

| Domain               | What it does                                                                      | Relation to NLP        |
| -------------------- | --------------------------------------------------------------------------------- | ---------------------- |
| **Computer Vision**  | Enables machines to "see" like humans (e.g., image recognition, object detection) | N/A                    |
| **Machine Learning** | Machines "learn" from data (e.g., supervised, unsupervised learning)              | Backbone of modern NLP |
| **NLP**              | Machines interpret, understand, and generate language                             | Core focus             |

---

### Why NLP is Important for Data Science

Data scientists use NLP to:

1. Extract insights from large volumes of text (emails, reviews, articles).
2. Analyze sentiment, classify topics, summarize content.
3. Automate manual processes like tagging, filtering, translation.

---

## History of NLP

### 1. **Rule-Based Era** (1950s–1980s)

* Early NLP systems used manually crafted **grammar rules**.
* Example: **ELIZA**, an early chatbot that mimicked human conversation using pattern matching.

### 2. **Statistical Era** (1990s–2010s)

* Rise of **Statistical Machine Translation (SMT)**.
* Shift from hand-written rules to models trained on data.
* Example: SMT systems like IBM Models used probability and statistics to translate text.

### 3. **Deep Learning & Modern NLP** (2015 onwards)

* Neural networks (especially **RNNs**, **LSTMs**) replaced earlier models.
* **Transformers** revolutionized NLP: Parallelization + Context awareness.
* Examples: **BERT**, **GPT**, **T5**, **XLNet**, **LLMs** in general.

---

## NLP Techniques Explained

### 1. **Rule-Based Techniques**

* Built using linguistic rules (e.g., if a word is “good,” tag sentiment as positive).
* Suitable for small datasets.
* Not scalable for real-world messy language.

### 2. **Statistical Techniques**

* Use of probability, statistics (like n-grams, Bayesian models).
* Example: Naive Bayes for text classification.

### 3. **Machine Learning (ML) Techniques**

* Supervised ML: Uses labeled data (e.g., spam vs. non-spam).
* Unsupervised ML: Finds patterns in unlabeled data
* Example: NMF (Non Negative Matrix Fsctorization) for text modeling

### 4. **Neural Network & Deep Learning**

* **RNNs**, **LSTMs**: Good for sequential data but limited in long-term context.
* **Transformers**: Solve the long-context problem using self-attention.
* Foundation for **LLMs** like GPT, BERT.

---

## Architectures in NLP

### ➤ Encoder-only models (e.g., BERT)

* Focus on understanding input text (used in classification, NER).
* Don’t generate text.

### ➤ Decoder-only models (e.g., GPT)

* Focus on generating new text based on input prompt.
* Used in chatbots, text generation.

### ➤ Encoder-Decoder models (e.g., T5, BART)

* Good for translation, summarization.
* Encode input → Decode output.

---

## Word Representations in NLP

* **Word Embeddings** = Vector representations of words.

  * Examples: **Word2Vec**, **GloVe**, **BERT**, **MiniLM**
* Similar meanings have similar vectors (semantic similarity).
* Foundation for most NLP tasks.

---

## NLP Libraries & Tools

| Library                       | Purpose                                                           |
| ----------------------------- | ----------------------------------------------------------------- |
| **Pandas**                    | Data manipulation and preprocessing                               |
| **spaCy**                     | Industrial-strength NLP pipeline (tokenization, POS tagging, NER) |
| **Scikit-learn**              | Machine learning algorithms (SVM, Naive Bayes)                    |
| **NLTK**                      | Classic NLP tasks (tokenization, stemming, corpora)               |
| **VADER**                     | Pre-built sentiment analyzer for social media text                |
| **Hugging Face Transformers** | Provides pretrained transformer models like BERT, GPT, etc.       |

---

## 📚 Common NLP Applications

| Task                               | Description                                        |
| ---------------------------------- | -------------------------------------------------- |
| **Text Classification**            | Categorize text (e.g., spam vs. not spam)          |
| **Sentiment Analysis**             | Detect emotions (positive, negative)               |
| **Named Entity Recognition (NER)** | Find entities like names, dates, places            |
| **Text Summarization**             | Generate a summary from input text                 |
| **Topic Modeling**                 | Discover abstract topics in documents              |
| **Text Generation**                | Generate human-like text (chatbots, story writing) |
| **Recommender Systems**            | Suggest content based on user interests using NLP  |


