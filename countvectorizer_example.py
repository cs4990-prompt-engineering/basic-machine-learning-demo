from sklearn.feature_extraction.text import CountVectorizer

# Simple "Hello World" example of CountVectorizer
texts = [
    "hello world",
    "hello python", 
    "world of machine learning"
]

# Create CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the texts
X = vectorizer.fit_transform(texts)

# Print results
print("Original texts:")
for i, text in enumerate(texts):
    print(f"{i}: {text}")

print(f"\nVocabulary: {vectorizer.get_feature_names_out()}")

print(f"\nCount matrix:")
print(X.toarray())

print(f"\nVocabulary mapping:")
for word, index in vectorizer.vocabulary_.items():
    print(f"'{word}' -> column {index}")
