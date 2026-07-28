import os
from groq import Groq
from dotenv import load_dotenv
from prompts import get_structured_prompt

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# -----------------------------
# Symptom Extraction
# -----------------------------

def extract_symptoms(user_input):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Extract key clinical symptoms from the input."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def run_reasoning(user_input):

    clinical_keywords = [
        "patient",
        "pain",
        "treatment",
        "symptom"
        "radiotherapy"
    ]

    # Check if query is clinical-related
    if not any(word in user_input.lower() for word in clinical_keywords):
        return "Please enter a healthcare or clinical-related query."


    prompt = get_structured_prompt(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
    {
        "role": "system",
        "content": (
            "You are a clinical reasoning assistant. "
            "Only answer healthcare and clinical-related queries. "
            "If the user asks unrelated questions, politely refuse."
        )
    },
    {
        "role": "user",
        "content": prompt
    }
],
        temperature=0.3
    )

    return response.choices[0].message.content
