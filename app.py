import streamlit as st
from utils.profile_parser import build_profile

QUESTIONS = [
    ("budget", "What is your monthly rent budget (HKD)?"),
    ("preferred_areas", "Which areas do you prefer? (comma separated)"),
    ("max_commute", "What is your maximum commute time (minutes)?"),
    ("sleep_time", "What is your sleep schedule? (early / normal / late)"),
    ("cleanliness", "How important is cleanliness? (1–5)"),
    ("noise_tolerance", "What is your noise tolerance? (1–5)"),
    ("cooking", "Do you cook often? (yes / no)"),
    ("room_type", "Do you prefer a private or shared room?")
]

st.set_page_config(page_title="HomeMatch MVP")
st.title("🏠 HomeMatch AI Onboarding")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

current_q = len(st.session_state.chat_history)

if current_q < len(QUESTIONS):
    key, question = QUESTIONS[current_q]
    st.chat_message("assistant").write(question)

    user_input = st.chat_input("Your answer")

    if user_input:
        st.session_state.chat_history.append((key, user_input))
        st.rerun()   # ✅ THIS IS ESSENTIAL
else:
    st.success("✅ Onboarding completed")

    profile = build_profile(st.session_state.chat_history)
    st.subheader("🧠 Generated User Profile")
    st.json(profile)
