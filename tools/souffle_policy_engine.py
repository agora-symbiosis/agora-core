import json, sys

def vitality(density, reciprocity, clarity):
    """Calcule la vitalité d’un fragment."""
    return density * 0.4 + reciprocity * 0.4 + clarity * 0.2

def compute_reciprocity(utterances):
    """Mesure la réciprocité entre humains et IA."""
    total = len(utterances)
    if total == 0:
        return 0.5
    human = sum(1 for u in utterances if u["role"] == "human")
    ai = sum(1 for u in utterances if u["role"] == "ai")
    if human + ai == 0:
        return 0.5
    ratio = human / (human + ai)
    return 1 - abs(0.5 - ratio) * 2

def main(cfg_path, log_path):
    """Évalue un fragment selon la configuration du Souffle."""
    cfg = json.load(open(cfg_path))
    log = json.load(open(log_path))

    density = log["metrics"]["density"]
    clarity = log["metrics"]["clarity"]
    reciprocity = compute_reciprocity(log["utterances"])
    vitality_score = vitality(density, reciprocity, clarity)

    result = {
        "fragment_id": log["fragment_id"],
        "metrics": {
            "density": density,
            "clarity": clarity,
            "reciprocity": reciprocity,
            "vitality": vitality_score
        }
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
