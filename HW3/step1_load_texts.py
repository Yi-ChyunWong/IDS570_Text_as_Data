from pathlib import Path

TEXT_DIR = Path("texts")

# Collect all .txt files
files = sorted(TEXT_DIR.glob("*.txt"))

print(f"Found {len(files)} .txt files.")

# Print the first few filenames
print("First 10 files:")
for f in files[:10]:
    print(" ", f)

# Read one example file
example_file = files[0]

with open(example_file, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("\nReading file:")
print(example_file)
print("-" * 40)
print("Number of characters:", len(text))
print("\nFirst 1,000 characters:\n")
print(text[:1000])