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
    {"role": "user", "content": f"""You are an experienced Technical Writer and documentation reviewer.

Analyze the following Markdown documentation and return a structured report with exactly these three sections:

## Clarity
Is the text written clearly? Are there any confusing or unclear parts?

## Missing Information
What important information is missing that a reader would expect?

## Inconsistent Terminology
Are terms used inconsistently (e.g. capitalization, different names for the same thing)?

Here is the documentation:

{inhalt}"""}
    ]
)

print(antwort.content[0].text)

with open("report.md", "w") as report_datei:
    report_datei.write(antwort.content[0].text)

print("\n✅ Report gespeichert als report.md")
