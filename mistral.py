import os
from dotenv import load_dotenv
load_dotenv()

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-2506"

client = Mistral(api_key=api_key)
system_prompt = """Use the Semantic HTML and class information to create a JSON representation of the webpage content. Reply with just the json representation and no other text."""

def chat(text):
    """Ask a question to the Mistral AI model and return the response."""
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "user", "content": text},
            {"role": "system", "content": system_prompt}
        ]
    )
    return response

if __name__ == "__main__":
    chat("<html><tr><td>Hello, world!</td></tr></html>")