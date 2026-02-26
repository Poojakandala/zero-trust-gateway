class RiskEngine:
    def calculate_score(self, features):
        freq = features.get("freq", 1)
        depth = features.get("path_depth", 1)
        hour = features.get("hour", 12)

        score = 0.0

        # High request rate → high risk
        if freq > 50:
            score += 0.5
        elif freq > 20:
            score += 0.3
        else:
            score += 0.1

        # Deep API probing → suspicious
        if depth > 4:
            score += 0.3
        else:
            score += 0.1

        # Late night attack window
        if 0 <= hour <= 5:
            score += 0.2

        return min(score, 1.0)
