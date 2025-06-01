# Multi-Agent AI System

This project implements a multi-agent AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, and routes it to the appropriate agent. The system maintains shared context (e.g., sender, topic, last extracted fields) to enable chaining and traceability.

## Project Structure

```
work/
│
├── agents/
│   ├── classifier_agent.py
│   ├── json_agent.py
│   └── email_agent.py
│
├── shared_memory.py
├── pdf_utils.py
├── intent_detection.py
├── main.py
├── requirements.txt
├── README.md
├── Demo_input.txt
└── ...
```

## Features
- **Classifier Agent**: Classifies input (PDF, JSON, Email), detects intent, routes to the correct agent, and logs to shared memory.
- **JSON Agent**: Accepts structured JSON, extracts/reformats to a target schema, flags anomalies or missing fields.
- **Email Agent**: Accepts email content, extracts sender/intent/urgency, formats for CRM-style usage.
- **Shared Memory**: Uses SQLite for context sharing and traceability across agents.

## Example Inputs
See `Demo_input.txt` for ready-to-use examples:
- JSON: `{ "id": "12", "amount": "2500", "date": "2025-05-03", "customer": "Dhruv" }`
- Email: `From: alice@example.com ...`
- PDF: `28_abstract.pdf`

## Setup & Usage
1. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the system**
   ```sh
   python main.py
   ```
3. **Paste your input** (JSON, Email text, or PDF path) when prompted.

## Tech Stack
- Python
- SQLite (for shared memory)
- [Ollama](https://ollama.com/) (optional, for local LLM intent detection)
- pdfplumber, pydantic, python-dotenv

