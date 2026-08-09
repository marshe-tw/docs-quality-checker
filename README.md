# Docs-Quality-Checker

A Python tool that analyzes Markdown documentation using the Claude API and generates a structured quality report — built to learn API integration, prompt engineering, and automated documentation review.

## About this project

This project was built as a learning exercise to practice:

- **Python fundamentals** – reading files, working with environment variables
- **Claude API integration** – sending structured prompts and handling responses
- **Prompt engineering** – designing prompts that return consistent, structured output
- **Secure API key handling** – using environment variables instead of hardcoding secrets

## What it checks

- **Clarity** – Is the content easy to understand?
- **Missing Information** – What important details are missing?
- **Inconsistent Terminology** – Are terms used inconsistently (e.g. capitalization, naming)?

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

3. Run the checker on any Markdown file:
```bash
   python3 checker.py example.md
```

## Example

Input: `example.md` – a guide on creating strong passwords
Output: `report.md` – a structured quality report

## Tech stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Claude API (Anthropic) | Documentation analysis |
| Markdown | Input/output format |

## What I learned

This was my first Python project. I learned how to work with files in Python, use environment variables to keep API keys secure, call the Claude API with structured prompts to get consistent output, and handle command-line arguments to make the tool flexible for any input file.

## Author

**Mohamed Arshe** – Technical Writer
[LinkedIn](https://linkedin.com/in/mohamed-arshe-083b712ba) · [GitHub](https://github.com/marshe-tw)