import os
from anthropic import Anthropic

api_key = os.environ.get("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

with open("example.md", "r") as datei:
    inhalt = datei.read()

antwort = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
    {"role": "user", "content": f"""Du bist ein erfahrener Technical Writer und Dokumentations-Reviewer.

Analysiere die folgende Markdown-Dokumentation und gib einen strukturierten Report zurück mit genau diesen drei Abschnitten:

## Klarheit
Ist der Text verständlich geschrieben? Gibt es verwirrende oder unklare Stellen?

## Fehlende Informationen
Welche wichtigen Informationen fehlen, die ein Leser erwarten würde?

## Inkonsistente Begriffe
Werden Begriffe uneinheitlich verwendet (z.B. Groß-/Kleinschreibung, unterschiedliche Bezeichnungen für dasselbe)?

Hier ist die Dokumentation:

{inhalt}"""}
    ]
)

print(antwort.content[0].text)

with open("report.md", "w") as report_datei:
    report_datei.write(antwort.content[0].text)

print("\n✅ Report gespeichert als report.md")
