from transformers import pipeline

# Zero-shot sınıflayıcıyı yükle (tek seferlik)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def filter_by_relevance(text_list, target_topic="law", threshold=0.8):
    """
    Verilen metin listesindeki, hedef konuyla ilgisiz satırları eleyin.
    """
    if not text_list:
        return [], []

    candidate_labels = [target_topic]

    relevant = []
    irrelevant = []

    for text in text_list:
        result = classifier(text, candidate_labels)
        score = result["scores"][0]  # yalnızca 1 label olduğundan

        if score >= threshold:
            relevant.append(text)
        else:
            irrelevant.append(text)

    return relevant, irrelevant
# Placeholder for domain relevance scoring
