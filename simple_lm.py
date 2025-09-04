from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


input_data = [
    ["I love to read"], 
    ["The quick brown fox"], 
    ["I prefer tea over"], 
    ["Machine learning is an interesting"], 
    ["Cal Poly Pomona has strong science"], 
]

output_data = [
    "books", 
    "jumps", 
    "coffee",
    "field", 
    "majors", 
]

# process the input data using count vectorizer
print(input_data)

input_data_processed = []
for data_row in input_data:    
    input_data_processed.append(data_row[0])

print(input_data_processed)

# vectorizer = CountVectorizer()
vectorizer = TfidfVectorizer()
input_data_vectorized = vectorizer.fit_transform(input_data_processed)
print(input_data_vectorized)

print(f"\nVocabulary: {vectorizer.get_feature_names_out()}")
print(f"\nCount matrix:")
print(input_data_vectorized.toarray())


model = svm.SVC(probability=True)
model.fit(input_data_vectorized, output_data)

test_data = vectorizer.transform(["I love to read", "The quick brown fox", "Cal Poly Pomona has science"])
probabilities = model.predict_proba(test_data)[0]
print(probabilities)

res = model.predict(test_data)
print(res)

# Sample from the distribution to get a random prediction
random_prediction = np.random.choice(model.classes_, p=probabilities)
print("Random Prediction:", random_prediction)
