from src.utils import log_error

from groq import Groq

from src.prompts import get_structured_prompt
from src.config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS
)


client = Groq(
    api_key=GROQ_API_KEY
)


# -----------------------------
# Symptom Extraction
# -----------------------------

def extract_symptoms(user_input):

    response = client.chat.completions.create(
    
 
        model=MODEL_NAME,
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
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content

def run_reasoning(user_input):
    
    


    clinical_keywords = [
        "patient",
        "pain",
        "treatment",
        "symptom",
        "radiotherapy"
    ]

    # Check if query is clinical-related
    if not any(word in user_input.lower() for word in clinical_keywords):
        return "Please enter a healthcare or clinical-related query."


    prompt = get_structured_prompt(user_input)

    try:
       
       response = client.chat.completions.create(
         model=MODEL_NAME,
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
        temperature=TEMPERATURE
    )
    

       return response.choices[0].message.content


    except Exception as e:
       log_error(e)
       return "Sorry, something went wrong while contacting the AI service. Please try again later."

 
   