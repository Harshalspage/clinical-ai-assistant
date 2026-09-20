import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Configuration
MODEL_NAME = "llama-3.1-8b-instant"

# LLM Parameters
TEMPERATURE = 0.3
MAX_TOKENS = 1024