import streamlit as st
from src.reasoning import run_reasoning
from src.validation import validate_input
   
st.set_page_config(page_title="Clinical Reasoning Assistant")

st.title("🧠 Clinical Reasoning Assistant")

user_input = st.text_area(
    "Enter Clinical Case"
)

if st.button("Analyze"):
    
    is_valid, message = validate_input(user_input)

    if is_valid:

        result = run_reasoning(user_input)

        st.subheader("Structured Output")

        st.write(result)

    else:
        st.warning(message)

