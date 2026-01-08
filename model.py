from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

LABELS = ["credible", "misleading"]

def score_headline(headline: str):
    result = classifier(headline, LABELS, multi_label=False)
    scores = dict(zip(result["labels"], result["scores"]))
    return {
        "headline": headline,
        "scores": scores,
        "credibility": round(scores.get("credible", 0)*100,1)
    }
