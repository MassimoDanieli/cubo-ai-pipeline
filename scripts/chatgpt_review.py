import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    files = sys.argv[1:]
    for file in files:
        content = read_file(file)
        print(f"\n## Review for: `{file}`\n")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Sei un esperto sviluppatore. Fai una code review breve ma costruttiva di questo file HTML/JS/Python."
                },
                {
                    "role": "user",
                    "content": f"File:\n\n{content}"
                }
            ],
            temperature=0.3,
            max_tokens=800
        )
        print(response["choices"][0]["message"]["content"])
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()

