def get_structured_prompt(user_input):
    return f"""
You are a clinical reasoning assistant.

Analyze the clinical input and provide structured reasoning.

Input:
{user_input}

Output format:

1. Identified Conditions:
2. Key Symptoms:
3. Possible Causes:
4. Suggested Actions:
5. Confidence Level:

Keep the response concise and structured.
"""