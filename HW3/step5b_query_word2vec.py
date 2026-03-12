from pathlib import Path
from gensim.models import Word2Vec

model_path = Path("models") / "w2v_full.bin"
model = Word2Vec.load(str(model_path))

seed = "merchant"

if seed not in model.wv:
    print(f"'{seed}' not found in the model vocabulary.")
    print("This usually means min_count is too high or the corpus is too small.")
else:
    print(f"Top 30 words similar to '{seed}':")
    for word, score in model.wv.similar_by_word(seed, topn=30):
        print(f"  {word:20s} {score:.3f}")