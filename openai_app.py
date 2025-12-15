# First program
# Pricing reference (optional for students)
# https://platform.openai.com/docs/pricing?latest-pricing=batch

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
    model="gpt-5-nano",
    input="Hi, My name is Shikha"
)

# output_text extracts plain text from the model response
print(f"Response--{response.output_text}")

response = client.responses.create(
    model="gpt-5-nano",
    input="Hey, now tell my name"
)

# output_text extracts plain text from the model response
print(f"Response--{response.output_text}")


# ---------------------------
# Example 2: Another call, stateless
# ---------------------------

# instructions = system-style instruction for this request only
# reasoning = optional reasoning budget (used by models with reasoning capability)
response = client.responses.create(
    model="gpt-5-nano",
    reasoning={"effort": "low"},   # request low reasoning effort
    instructions="Talk like a pirate.",  # behave like a pirate for this request
    input="Can you tell me what is my name?",
)

print(f"Response--{response.output_text}")
