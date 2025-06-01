import os
import ollama

def detect_intent(text: str) -> str:
    # Try Ollama first
    try:
        response = ollama.chat(model='llama3', messages=[
            {"role": "user", "content": f"Classify this text as: Invoice, RFQ, Complaint, Regulation, or Unknown.\n\nText: {text}"}
        ])
        intent = response['message']['content'].strip()
        if intent:
            return intent
    except Exception:
        pass
    # Rule-based fallback
    text_lower = text.lower()
    if 'invoice' in text_lower:
        return 'Invoice'
    if 'request for quote' in text_lower or 'rfq' in text_lower:
        return 'RFQ'
    if 'complaint' in text_lower:
        return 'Complaint'
    if 'regulation' in text_lower:
        return 'Regulation'
    return 'Unknown'
