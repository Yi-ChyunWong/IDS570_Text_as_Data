from pathlib import Path
import nltk
from gensim.utils import simple_preprocess
import json

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

#
# Tier definitions (from Step 6)


TIER_A = {
    "merchant", "merchants",
    "marchant", "marchants"
}

TIER_B = {
    "factor", "chapman",
    "adventurer", "adventurers",
    "venturer", "venturers",
    "staple", "staplers",
    "trade", "purser"
}

TIER_C = {
    "clothier", "clothyer",
    "tailor", "tayler",
    "haberdasher",
    "goldsmith",
    "vintner",
    "brewer",
    "banker",
    "grazier",
    "jeweller"
}


# Load and process texts


TEXT_DIR = Path("texts")
txt_paths = sorted(TEXT_DIR.glob("*.txt"))

TARGET_WORDS = 120
MIN_WORDS = 5
MAX_WORDS = 200

def chunk_text(text, target_words=120):
    sentences = nltk.sent_tokenize(text)

    chunks = []
    current = []
    current_len = 0

    for sent in sentences:
        words = sent.split()
        if not words:
            continue

        if current_len + len(words) > target_words and current:
            chunks.append(" ".join(current))
            current = []
            current_len = 0

        current.append(sent)
        current_len += len(words)

    if current:
        chunks.append(" ".join(current))

    return chunks

labeled = []

print(f"Processing {len(txt_paths)} files...")

for path in txt_paths:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    chunks = chunk_text(text, TARGET_WORDS)

    for c in chunks:
        tokens = simple_preprocess(c, deacc=True)
        n_tokens = len(tokens)

        if not (MIN_WORDS <= n_tokens <= MAX_WORDS):
            continue

        token_set = set(tokens)

        if token_set & (TIER_A | TIER_B):
            label = 1   # CORE
        elif token_set & TIER_C:
            label = 2   # MAYBE
        else:
            label = 0   # NEG

        labeled.append((c, label))

print("Total chunks labeled:", len(labeled))


# Save labeled data


Path("data").mkdir(exist_ok=True)

with open(Path("data") / "merchant_labeled_chunks.json", "w", encoding="utf-8") as f:
    json.dump(labeled, f, ensure_ascii=False)

print("Saved labeled chunks to data/merchant_labeled_chunks.json")

print("\nLabel distribution:")
print(f"  CORE (1): {sum(1 for _, y in labeled if y == 1)}")
print(f"  NEG  (0): {sum(1 for _, y in labeled if y == 0)}")
print(f"  MAYBE(2): {sum(1 for _, y in labeled if y == 2)}")

# Sample one from each category
for label_name, label_val in [("CORE", 1), ("MAYBE", 2), ("NEG", 0)]:
    example = next((text for text, y in labeled if y == label_val), None)
    if example:
        print(f"\n{label_name} example (first 200 chars):")
        print(example[:200])