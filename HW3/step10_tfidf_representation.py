import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
DATA_DIR = Path("data")

#We now load the datasets we prepared at the end of last week (step 9)
with open(DATA_DIR / "train_core_vs_neg.json", "r", encoding="utf-8") as f:
    train_data = json.load(f)

with open(DATA_DIR / "test_core_vs_neg.json", "r", encoding="utf-8") as f:
    test_data = json.load(f)

# Separate texts and labels
X_train_texts = [t for (t, y) in train_data]
y_train = [y for (t, y) in train_data]

X_test_texts = [t for (t, y) in test_data]
y_test = [y for (t, y) in test_data]

print("Train size:", len(X_train_texts))
print("Test size :", len(X_test_texts))

##### ==> See explanation [A] below

vectorizer = TfidfVectorizer(
    lowercase=True,
    min_df=5,        # ignore very rare words
    max_df=0.9       # ignore extremely common words; Explanation [B]
)
X_train = vectorizer.fit_transform(X_train_texts)
X_test = vectorizer.transform(X_test_texts)

print("TF-IDF matrix shapes:")
print("  Train:", X_train.shape)
print("  Test :", X_test.shape)

#####  ==> See explanation [C] below