import os
import openai
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_commit_messages():
    result = subprocess.run(
        ["git", "log", "-10", "--pretty=format:%h %s"],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def generate_changelog(commits):
    messages = [
        {
            "role": "system",
            "content": "Sei uno sviluppatore DevOps. Genera un changelog leggibile e ordinato, breve ma informativo, da questi commit."
        },
        {
            "role": "user",
            "content": f"Commit recenti:\n\n{commits}"
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3,
        max_tokens=600
    )
    return response.choices[0].message.content

def main():
    commits = get_commit_messages()
    changelog = generate_changelog(commits)

    with open("CHANGELOG.md", "w") as f:
        f.write("# 📝 Changelog (generato automaticamente)\n\n")
        f.write(changelog)

    print("✅ Changelog aggiornato.")

if __name__ == "__main__":
    main()
