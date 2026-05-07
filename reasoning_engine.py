import os
from groq import Groq
from dotenv import load_dotenv
from prompts import get_structured_prompt

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def run_reasoning(user_input):

    prompt = get_structured_prompt(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a clinical reasoning assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
