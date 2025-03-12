import os
from groq import Groq

def ask_question(api_key, question):
    """Ask a question to the Groq API."""
    client = Groq(api_key=api_key)
    system_prompt = """consider you are the best cricketer in world help this question."""
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        model="mixtral-8x7b-32768"
    )
    
    print("\nResponse:", response.choices[0].message.content)

def main():
    api_key = "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"
    question = input("which team won the champion trophy in 2025: ")
    ask_question(api_key, question)

if __name__ == "__main__":
    main()
