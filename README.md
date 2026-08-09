# Docs-Quality-Checker

A Python tool that analyzes Markdown documentation using the Claude API and generates a quality report.

## What it does

The tool reads a Markdown file and checks it for:
- **Clarity** – Is the content easy to understand?
- **Missing information** – What important details are missing?
- **Inconsistent terminology** – Are terms used inconsistently (e.g. capitalization, naming)?

## How it works

1. The script reads a Markdown file
2. It sends the content to Claude with a structured prompt
3. Claude analyzes the documentation and returns a report
4. The report is saved as `report.md`

## Setup

1. Install the required library:
```bash
   pip3 install anthropic
```

2. Set your Anthropic API key as an environment variable:
```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
```

3. Run the checker:
```bash
   python3 checker.py
```

## Example

Input: `example.md` – a guide on creating strong passwords
Output: `report.md` – a structured quality report

## What I learned

This was my first Python project. I learned how to:
- Work with files in Python
- Use environment variables to keep API keys secure
- Call the Claude API and structure prompts for consistent output

## Tech stack

- Python 3
- Claude API (Anthropic)