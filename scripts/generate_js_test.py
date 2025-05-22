import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    with open("index.html", "r") as f:
        html = f.read()

    prompt = f"""
Hai davanti una pagina HTML che contiene un input numerico e un bottone per calcolare il volume di un cubo dato un lato `n`.

Genera un test automatico JavaScript moderno (con Jest o simile), che:
- Simuli l'inserimento di un valore (es. 5)
- Clicchi sul bottone
- Verifichi che il contenuto del tag con ID "risultato" sia "Il volume è: 125"

Ecco il codice HTML:

{html}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Genera un test automatico JavaScript ben formattato e funzionante"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    test_code = response.choices[0].message.content

    os.makedirs("__tests__", exist_ok=True)
    with open("__tests__/test_volume.js", "w") as f:
        f.write(test_code)

    print("✅ Test JS generato in __tests__/test_volume.js")

if __name__ == "__main__":
    main()

