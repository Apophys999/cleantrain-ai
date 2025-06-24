from sentence_transformers import SentenceTransformer, util
import torch
import numpy as np

# Modeli bir kez yükle
model = SentenceTransformer('all-MiniLM-L6-v2')

def remove_duplicates(text_list, similarity_threshold=0.9):
    """
    Verilen metin listesindeki benzer satırları kaldırır.
    """
    if len(text_list) < 2:
        return text_list, []

    embeddings = model.encode(text_list, convert_to_tensor=True, show_progress_bar=False)

    to_remove = set()
    for i in range(len(text_list)):
        if i in to_remove:
            continue
        similarities = util.cos_sim(embeddings[i], embeddings[i+1:])[0]
        for j, score in enumerate(similarities):
            if score >= similarity_threshold:
                to_remove.add(i + 1 + j)

    cleaned_texts = [txt for idx, txt in enumerate(text_list) if idx not in to_remove]
    removed_texts = [txt for idx, txt in enumerate(text_list) if idx in to_remove]

    return cleaned_texts, removed_texts
# Placeholder for embedding-based duplicate remover
