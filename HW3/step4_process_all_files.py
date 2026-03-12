from pathlib import Path
import nltk
from gensim.utils import simple_preprocess

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

TEXT_DIR = Path("texts")
txt_paths = sorted(TEXT_DIR.glob("*.txt"))

TARGET_WORDS = 120
MIN_WORDS = 5
MAX_WORDS = 200

all_chunks = []
all_token_lists = []

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

print(f"Found {len(txt_paths)} text files.")
print()

for path in txt_paths:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    chunks = chunk_text(text, TARGET_WORDS)

    for c in chunks:
        tokens = simple_preprocess(c, deacc=True)
        n_tokens = len(tokens)

        # Filter by length
        if MIN_WORDS <= n_tokens <= MAX_WORDS:
            all_chunks.append(c)
            all_token_lists.append(tokens)

print("Total chunks kept (after filtering):", len(all_chunks))