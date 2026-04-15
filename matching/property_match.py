import pandas as pd

DATA_PATH = "data/properties.xlsx"


def match_properties(user_profile):
    """
    Match and rank properties based on the user profile.
    Returns a list of scored and explainable property results.
    """

    df = pd.read_excel(DATA_PATH)
    results = []

    for _, row in df.iterrows():
        score = 0
        reasons = []

        # 1. Budget fit
        if row["rent"] <= user_profile["budget"]:
            score += 40
            reasons.append("Within budget")
        else:
            reasons.append("Above budget")

        # 2. Area preference
        if row["area"] in user_profile["preferred_areas"]:
            score += 30
            reasons.append("Located in preferred area")

        # 3. Commute constraint
        if row["commute_time"] <= user_profile["max_commute"]:
            score += 20
            reasons.append("Commute time acceptable")

        # 4. Room type preference
        if row["room_type"] == user_profile["room_type"]:
            score += 10
            reasons.append("Room type matches preference")

        results.append({
            "area": row["area"],
            "rent": row["rent"],
            "commute_time": row["commute_time"],
            "room_type": row["room_type"],
            "score": score,
            "reasons": reasons
        })

    # Rank by score (descending)
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results
