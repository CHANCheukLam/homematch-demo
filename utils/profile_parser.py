import re

def build_profile(chat_history):
    profile = {}

    for key, value in chat_history:

        if key in ["budget", "max_commute", "cleanliness", "noise_tolerance"]:
            number = re.search(r"\d+", value)
            profile[key] = int(number.group()) if number else None

        elif key == "preferred_areas":
            profile[key] = [v.strip() for v in value.split(",")]

        elif key == "cooking":
            profile[key] = value.lower().startswith("y")

        else:
            profile[key] = value.lower()

    return profile