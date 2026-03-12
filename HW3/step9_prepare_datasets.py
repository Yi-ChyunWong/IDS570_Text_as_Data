import json
from pathlib import Path
import random

random.seed(42) # For reproducibility--same random sample each time [see (*) below]

DATA_PATH = Path("data") / "merchant_labeled_chunks.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    labeled = json.load(f)

core = [(t, 1) for (t, y) in labeled if y == 1]
neg  = [(t, 0) for (t, y) in labeled if y == 0]
maybe = [t for (t, y) in labeled if y == 2]

print("Loaded:")
print("  CORE:", len(core))
print("  NEG :", len(neg))
print("  MAYBE:", len(maybe))

###### => NEG step [see explanation below]
neg_sample = random.sample(neg, len(core))

training_data = core + neg_sample
random.shuffle(training_data)

print("Training set size (CORE + NEG):", len(training_data))

### Split the data into train and test sets:

split = int(0.8 * len(training_data))
train_data = training_data[:split]
test_data  = training_data[split:]

print("Train size:", len(train_data))
print("Test size :", len(test_data))
print("MAYBE size:", len(maybe))

# Save the datasets:

Path("data").mkdir(exist_ok=True)

with open(Path("data") / "train_core_vs_neg.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, ensure_ascii=False)

with open(Path("data") / "test_core_vs_neg.json", "w", encoding="utf-8") as f:
    json.dump(test_data, f, ensure_ascii=False)

with open(Path("data") / "maybe_texts.json", "w", encoding="utf-8") as f:
    json.dump(maybe, f, ensure_ascii=False)

print("Saved training, test, and MAYBE datasets.")