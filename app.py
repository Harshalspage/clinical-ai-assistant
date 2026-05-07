import streamlit as st
from reasoning_engine import run_reasoning

st.set_page_config(page_title="Clinical Reasoning Assistant")

st.title("🧠 Clinical Reasoning Assistant")

user_input = st.text_area(
    "Enter Clinical Case"
)

if st.button("Analyze"):

    if user_input:

        result = run_reasoning(user_input)

        st.subheader("Structured Output")

        st.write(result)

    else:
        st.warning("Please enter a clinical case.")