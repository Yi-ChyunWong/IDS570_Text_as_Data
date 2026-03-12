from pathlib import Path
import json

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score
)

from sklearn.feature_extraction.text import TfidfVectorizer

DATA_DIR = Path("data")

with open(DATA_DIR / "train_core_vs_neg.json", "r", encoding="utf-8") as f:
    train_data = json.load(f)

with open(DATA_DIR / "test_core_vs_neg.json", "r", encoding="utf-8") as f:
    test_data = json.load(f)

X_train_texts = [t for (t, y) in train_data]
y_train = [y for (t, y) in train_data]

X_test_texts = [t for (t, y) in test_data]
y_test = [y for (t, y) in test_data]

vectorizer = TfidfVectorizer(
    lowercase=True,
    min_df=5,
    max_df=0.9
)

X_train = vectorizer.fit_transform(X_train_texts)
X_test = vectorizer.transform(X_test_texts)

# clf = LogisticRegression(
#     max_iter=1000,
#     penalty='l1',
#     solver='liblinear'
# )
clf = LogisticRegression(
    max_iter=1000,
    l1_ratio=1,
    solver='liblinear'
)

clf.fit(X_train, y_train)

#test set predictions
y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test)[:, 1]

cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(cm)

print("\nClassification report:")
print(classification_report(y_test, y_pred))

###ROC AUC
auc = roc_auc_score(y_test, y_prob)
print("ROC AUC:", round(auc, 3))

print("\nNumber of non-zero coefficients:", (clf.coef_[0] != 0).sum())

top_pos_words = sorted(
    zip(vectorizer.get_feature_names_out(), clf.coef_[0]),
    key=lambda x: x[1],
    reverse=True
)[:15]

print("\nTop 15 positive words:")
for word, coef in top_pos_words:
    print(f"  {word}: {coef:.3f}")

top_neg_words = sorted(
    zip(vectorizer.get_feature_names_out(), clf.coef_[0]),
    key=lambda x: x[1]
)[:15]

print("\nTop 15 negative words:")
for word, coef in top_neg_words:
    print(f"  {word}: {coef:.3f}")

from pathlib import Path
import joblib

MODEL_DIR = Path.cwd() / "models"
MODEL_DIR.mkdir(exist_ok=True)

joblib.dump(vectorizer, MODEL_DIR / "tfidf_vectorizer_l1.joblib")
joblib.dump(clf, MODEL_DIR / "merchant_logreg_l1.joblib")

print("Saved TF-IDF vectorizer and classifier to /models/")