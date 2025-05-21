import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def save_review(content):
    os.makedirs(".gpt-review", exist_ok=True)
    filename = f".gpt-review/review-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    with open(filename, "w") as f:
        f.write(content)
    print(f"✅ Review salvata in: {filename}")

def main():
    files = sys.argv[1:]
    final_report = ""
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

        review = response.choices[0].message.content
        print(review)
        final_report += f"## Review for `{file}`\n\n{review}\n\n{'='*80}\n\n"

    save_review(final_report)

if __name__ == "__main__":
    main()

