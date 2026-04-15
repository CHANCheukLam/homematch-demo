import pandas as pd

DATA_PATH = "data/roommates.xlsx"


def match_roommates(user_profile):
    """
    Match and rank roommates based on lifestyle compatibility.
    Returns a list of compatibility scores with explanations.
    """

    df = pd.read_excel(DATA_PATH)
    results = []

    for _, row in df.iterrows():
        score = 0
        reasons = []

        # 1. Sleep schedule
        if row["sleep_time"] == user_profile["sleep_time"]:
            score += 30
            reasons.append("Same sleep schedule")

        # 2. Cleanliness similarity
        clean_diff = abs(row["cleanliness"] - user_profile["cleanliness"])
        if clean_diff == 0:
            score += 25
            reasons.append("Identical cleanliness standards")
        elif clean_diff == 1:
            score += 15
            reasons.append("Similar cleanliness standards")

        # 3. Noise tolerance similarity
        noise_diff = abs(row["noise_tolerance"] - user_profile["noise_tolerance"])
        if noise_diff == 0:
            score += 25
            reasons.append("Same noise tolerance")
        elif noise_diff == 1:
            score += 15
            reasons.append("Similar noise tolerance")

        # 4. Cooking habits
        if row["cooking"] == user_profile["cooking"]:
            score += 20
            reasons.append("Cooking habits match")

        results.append({
            "name": row["name"],
            "compatibility_score": score,
            "reasons": reasons
        })

    # Rank by compatibility (descending)
    results = sorted(results, key=lambda x: x["compatibility_score"], reverse=True)
    return results