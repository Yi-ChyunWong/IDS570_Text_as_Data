from pathlib import Path
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

TEXT_DIR = Path("texts")
txt_paths = sorted(TEXT_DIR.glob("*.txt"))

sample_path = txt_paths[0]

with open(sample_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Split text into sentences
sentences = nltk.sent_tokenize(text)

print("File:", sample_path)
print("Number of sentences:", len(sentences))
print()

# Group sentences into chunks of ~120 words
TARGET_WORDS = 120

chunks = []
current = []
current_len = 0

for sent in sentences:
    words = sent.split()
    if not words:
        continue

    # If adding this sentence would exceed the target, finalize the chunk
    if current_len + len(words) > TARGET_WORDS and current:
        chunks.append(" ".join(current))
        current = []
        current_len = 0

    current.append(sent)
    current_len += len(words)

# Add any leftover sentences
if current:
    chunks.append(" ".join(current))

print("Number of chunks:", len(chunks))

# Diagnostics on chunk length (rough word counts)
lengths = [len(c.split()) for c in chunks]
lengths_sorted = sorted(lengths)

print()
print("Approx word counts per chunk:")
print("  min:", min(lengths))
print("  median:", lengths_sorted[len(lengths_sorted)//2])
print("  max:", max(lengths))

lo, hi = 5, 200
in_range = sum(lo <= n <= hi for n in lengths)
print(f"Chunks with {lo}–{hi} words:", in_range)
print("Share in range:", round(in_range / len(lengths), 3))

print()
print("--- Chunk 1 preview (first 400 chars) ---")
print(chunks[0][:400])