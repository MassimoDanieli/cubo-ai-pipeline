 os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    files = sys.argv[1:]
    for file in files:
        content = read_file(file)
        print(f"\n## Review for: `{file}`\n")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Sei uno sviluppatore esperto. Fai una code review breve ma costruttiva del seguente file."
                },
                {
                    "role": "user",
                    "content": f"File: {file}\n\n{content}"
                }
            ],
            temperature=0.3
        )

        print(response.choices[0].message.content)
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()

