## **What is a Corpus?**

### Definition:

A **corpus** (plural: **corpora**) is a **collection of text documents** that are used for analysis, training models, or extracting insights.

In simple terms, think of a **corpus** as your **"text dataset"** — just like how you'd have a CSV of numbers for data analysis, a corpus is the **text equivalent**.

---

### **Why Is a Corpus Important?**

Because **text data is unstructured**, we need a standardized and clean way to:

* Store it
* Process it
* Analyze patterns, topics, or sentiment

A **corpus gives us the raw material** on which we apply all text analysis techniques like:

* Tokenization
* Sentiment analysis
* Topic modeling
* Word embeddings
* Chatbot training

---

## **When Do You Use a Corpus?**

| Task                        | Role of Corpus                                 |
| --------------------------- | ---------------------------------------------- |
| Text classification         | Acts as training/testing data                  |
| Sentiment analysis          | Contains all reviews or tweets                 |
| Language modeling           | Helps train models to understand language      |
| Translation / summarization | Supplies examples of text pairs or summaries   |
| Chatbot training            | Conversational corpora improve chatbot replies |

---

## **Example Corpus (for Sentiment Analysis)**

```python
corpus = [
    "I love this product!",
    "Worst customer service ever.",
    "Very fast delivery and great quality.",
    "Not worth the price.",
    "Amazing experience, would buy again!"
]
```

This list of 5 reviews is your **corpus**.

You can then:

* **Tokenize** each sentence
* **Clean** each review (remove punctuation, lowercasing)
* **Label** the sentiments (positive/negative)
* Train a **sentiment classifier** on this corpus

---

## Types of Corpora (by Purpose)

| Type                         | Description                                     | Example                                     |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------- |
| **General Language Corpora** | To understand common grammar, syntax, vocab     | British National Corpus (BNC)               |
| **Domain-Specific Corpora**  | Focused on medical, legal, or tech language     | Legal case documents                        |
| **Sentiment Corpora**        | Reviews labeled with positive/negative emotions | IMDB Movie Review dataset                   |
| **Conversational Corpora**   | Chat dialogues used in bots or AI agents        | Cornell Movie Dialogs, Facebook Chat Corpus |
| **Parallel Corpora**         | Text in one language and its translation        | EuroParl (English–French pairs)             |

---

## **How Is a Corpus Stored/Used in Practice?**

1. **In Files:**

   * Stored as `.txt`, `.json`, `.csv`
   * Often one document per line or row

2. **In Code (Python):**

   * As a **list of strings**
   * Or with labels for classification:

     ```python
     corpus = [
       ("I love this!", "positive"),
       ("This is bad", "negative")
     ]
     ```

3. **In NLP Libraries:**

   * **NLTK** and **spaCy** provide built-in corpora
   * You can also import your custom corpora for training models

     ```python
     import nltk
     from nltk.corpus import movie_reviews
     ```

---

## Corpus vs Document vs Text

| Term         | Meaning                                                |
| ------------ | ------------------------------------------------------ |
| **Corpus**   | A **collection** of text documents                     |
| **Document** | A single piece of text (e.g., one review, one article) |
| **Text**     | The raw language content (e.g., "I love Python")       |

---

## Summary

| Term    | Description                               |
| ------- | ----------------------------------------- |
| Corpus  | A collection of text documents            |
| Purpose | Used for analysis, training, or modeling  |
| Usage   | NLP tasks: sentiment, topics, translation |
| Tools   | Python, NLTK, spaCy, sklearn, etc.        |

Excellent question!

### **Is a Corpus Structured or Unstructured Data?**

By default, a **corpus is made up of *unstructured data*** — because it contains **raw text**, which:

* Has **no predefined format**
* Doesn’t follow rows and columns with specific labels
* Is written in **natural language** (like English, Hindi, etc.)

---

### Example: Unstructured Corpus

```python
corpus = [
    "This laptop is amazing!",
    "Not happy with the product.",
    "Delivery was quick and packaging was good.",
    "Too expensive for the quality."
]
```

There are no:

* Labels (like sentiment)
* Structure (like date, user ID, rating)

This is a **pure unstructured corpus**.

---

## When Can a Corpus Become Structured?

You can **transform** a corpus into **structured data** by:

* **Labeling** it (e.g., positive/negative sentiment)
* **Tokenizing** it (split into words)
* **Extracting features** (TF-IDF, word embeddings)
* **Storing it in tables or dataframes**

### Example: Structured Version

| Text                                         | Sentiment |
| -------------------------------------------- | --------- |
| "This laptop is amazing!"                    | Positive  |
| "Not happy with the product."                | Negative  |
| "Delivery was quick and packaging was good." | Positive  |
| "Too expensive for the quality."             | Negative  |

This is now **structured text data**, ready for:

* Machine learning
* Statistical analysis
* Dashboards

---

### Finally:

| Question              | Answer                                   |
| --------------------- | ---------------------------------------- |
| Is corpus structured? | ❌ No — it is **unstructured by default** |
| Can it be structured? | ✅ Yes — using preprocessing + labeling   |

Would you like to see a full Python example where we convert a raw corpus into structured format step by step?
