import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_commit_messages():
    result = subprocess.run(
        ["git", "log", "-10", "--pretty=format:%h %s"],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def generate_changelog(commits):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Sei uno sviluppatore DevOps. Genera un changelog leggibile, ordinato e professionale da questi commit:"
            },
            {
                "role": "user",
                "content": commits
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

def main():
    commits = get_commit_messages()
    changelog = generate_changelog(commits)

    with open("CHANGELOG.md", "w") as f:
        f.write("# 📝 Changelog (generato automaticamente)\n\n")
        f.write(changelog)

if __name__ == "__main__":
    main()

