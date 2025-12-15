# pip install ollama

import ollama

# ---------------------------
# Example 1: Basic call
# ---------------------------

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {"role": "user", "content": "Hi, my name is Shikha"}
    ]
)

print("Response--", response["message"]["content"])


# ---------------------------
# Example 2: Stateless behavior (same as OpenAI)
# ---------------------------

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {"role": "system", "content": "Talk like a pirate."},
        {"role": "user", "content": "Can you tell me what is my name?"}
    ]
)

print("Response--", response["message"]["content"])
