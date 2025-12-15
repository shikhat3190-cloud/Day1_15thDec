
"""

## Temperature vs Top-p

Use only one typically.
temperature = randomness of each token
top_p = model chooses from the smallest set of tokens whose probability adds up to p

max_output_tokens: Controls cost and length. Very important for students to understand.

"""
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
# Make sure your .env file contains:  OPENAI_API_KEY="your_api_key"
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()
# ---------------------------
# Example 1: Basic API call
# ---------------------------

# responses.create() sends a single query to the model.
# API calls are stateless: the model does NOT remember previous inputs.

response = client.responses.create(
    model="gpt-4o-mini",
    temperature=0.1,
    # Sampling parameters
    max_output_tokens=50,    # limit length of generated response
    # Instructions and input
    instructions="Act like a university professor.",
    input="Write a welcome message for my students.",
)

print(f"Response--{response.output_text}")

# from pprint import pprint
#
# pprint(response)

