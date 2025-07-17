## What Are N-grams?

An **N-gram** is a **sequence of N words** taken from a text.

It’s a way to **capture the context and structure** of the language — instead of analyzing words in isolation (like in Bag of Words), we look at **word pairs, triples, or more**.

---

## Types of N-grams:

| Type        | N  | Example (for sentence: “I love Python programming”) |
| ----------- | -- | --------------------------------------------------- |
| **Unigram** | 1  | `['I', 'love', 'Python', 'programming']`            |
| **Bigram**  | 2  | `['I love', 'love Python', 'Python programming']`   |
| **Trigram** | 3  | `['I love Python', 'love Python programming']`      |
| **4-gram+** | 4+ | `['I love Python programming']`, etc.               |

---

## Why Use N-grams?

| Goal                   | How N-grams Help                             |
| ---------------------- | -------------------------------------------- |
| Capture context        | Bigram "New York" ≠ Unigrams "New", "York"   |
| Improve model accuracy | Useful in sentiment analysis, spam detection |
| Detect common phrases  | Like "machine learning", "customer service"  |
| Language modeling      | Predict next word based on previous N words  |

---

## Real Example

### Input Text:

> "The food was very delicious"

| N-gram Type | Result                                                    |
| ----------- | --------------------------------------------------------- |
| Unigrams    | `['The', 'food', 'was', 'very', 'delicious']`             |
| Bigrams     | `['The food', 'food was', 'was very', 'very delicious']`  |
| Trigrams    | `['The food was', 'food was very', 'was very delicious']` |

---

## Python Example

```python
from sklearn.feature_extraction.text import CountVectorizer

text = ["The food was very delicious"]

# Bigrams
vectorizer = CountVectorizer(ngram_range=(2,2))
X = vectorizer.fit_transform(text)
print(vectorizer.get_feature_names_out())
# Output: ['food was' 'the food' 'very delicious' 'was very']
```

You can change `ngram_range=(1,1)` for Unigrams, `(3,3)` for Trigrams, or `(1,3)` to get all 1-grams to 3-grams.

---

## Summary

| Term    | N | Meaning                 | Use Case                           |
| ------- | - | ----------------------- | ---------------------------------- |
| Unigram | 1 | Single words            | Basic word frequency analysis      |
| Bigram  | 2 | Two consecutive words   | Phrase detection, context building |
| Trigram | 3 | Three consecutive words | Better context capture             |
| N-gram  | N | Any N-word combination  | Flexible for model accuracy        |

---

## **What is the Bag of Words (BoW) Model?**

### Definition:

The **Bag of Words** is a technique used in Natural Language Processing (NLP) to convert **text into numerical data**.

It:

* Creates a **vocabulary** of all unique words in a corpus.
* Represents each document as a **vector** that counts how often each word appears.
* **Ignores grammar and word order**, hence the term “bag”.

Imagine you "dump all the words into a bag" — and only care about **what words are in the bag**, and **how many times** they appear.

---

## Step-by-Step Explanation

Let’s go step by step using a simple example.

### Step 1: Prepare the Corpus

Let’s say we have 3 sentences (our **corpus**):

```python
corpus = [
    "I love Python",
    "Python is great",
    "I love coding"
]
```

---

### Step 2: Build the Vocabulary

We extract all **unique words** from the entire corpus:

```
Vocabulary = ['I', 'love', 'Python', 'is', 'great', 'coding']
```

This becomes the **basis for your columns** in the matrix.

---

### Step 3: Count the Words

Now for each sentence, count how many times each word appears from the vocabulary:

| Sentence        | I | love | Python | is | great | coding |
| --------------- | - | ---- | ------ | -- | ----- | ------ |
| I love Python   | 1 | 1    | 1      | 0  | 0     | 0      |
| Python is great | 0 | 0    | 1      | 1  | 1     | 0      |
| I love coding   | 1 | 1    | 0      | 0  | 0     | 1      |

This matrix is your **Bag of Words representation**.

Each **row is a document**, and each **column is a word** from your vocabulary.

---

## How It Works in Python (with Code)

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "I love Python",
    "Python is great",
    "I love coding"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
# Output: ['coding' 'great' 'is' 'love' 'python']

print(X.toarray())
# Output:
# [[0 0 0 1 1]
#  [0 1 1 0 1]
#  [1 0 0 1 0]]
```

Note: `CountVectorizer` automatically:

* Converts to lowercase
* Removes punctuation
* Tokenizes the words

---

## Why Do We Use Bag of Words?

| Purpose                 | How BoW Helps                         |
| ----------------------- | ------------------------------------- |
| **Text classification** | Emails → spam/ham                     |
| **Sentiment analysis**  | Reviews → positive/negative           |
| **Search engines**      | Match queries with relevant documents |
| **Language modeling**   | Predict the next word in a sentence   |

BoW transforms **text into features** that can be used in **machine learning algorithms**.

---

## Limitations of BoW

| Problem                          | Why It's a Challenge                         |
| -------------------------------- | -------------------------------------------- |
| **Ignores word order**           | “dog bites man” = “man bites dog”            |
| **Sparse vectors**               | For large vocabularies, most values are zero |
| **No semantic meaning**          | “good” and “great” are treated as different  |
| **Sensitive to vocabulary size** | New words in test data won’t be handled      |

---

## Comparison with Other Methods

| Method       | Keeps Word Order | Handles Meaning | Sparse? | Notes                        |
| ------------ | ---------------- | --------------- | ------- | ---------------------------- |
| **BoW**      | ❌ No             | ❌ No            | ✅ Yes   | Basic but fast               |
| **TF-IDF**   | ❌ No             | ❌ No            | ✅ Yes   | Highlights unique terms      |
| **Word2Vec** | ✅ Yes (somewhat) | ✅ Yes           | ❌ No    | Captures word relationships  |
| **BERT**     | ✅ Yes            | ✅ Deep meaning  | ❌ No    | Deep learning, very powerful |

---

## When to Use BoW

✅ Great for:

* Simple models (Naive Bayes, SVM)
* Small to medium datasets
* Baseline experiments

❌ Not ideal for:

* Context-sensitive tasks (like translation or sentiment from sarcasm)
* Deep semantic understanding

---

## Summary

| Feature          | Bag of Words                             |
| ---------------- | ---------------------------------------- |
| Converts text to | Vectors based on word count              |
| Ignores          | Word order and grammar                   |
| Simple to use    | Yes, quick to implement                  |
| Used in          | Classification, search, clustering       |
| Limitations      | Sparse vectors, lacks context or meaning |
