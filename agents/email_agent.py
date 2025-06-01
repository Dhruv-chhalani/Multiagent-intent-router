import re
from shared_memory import SharedMemory

class EmailAgent:
    def __init__(self, memory: SharedMemory):
        self.memory = memory

    def process(self, email_text: str):
        # Extract sender (simple regex for demo)
        sender = None
        match = re.search(r'From: (.+)', email_text)
        if match:
            sender = match.group(1).strip()
        # Extract intent (placeholder)
        intent = 'RFQ' if 'request for quote' in email_text.lower() else 'Unknown'
        # Extract urgency (placeholder)
        urgency = 'High' if 'urgent' in email_text.lower() else 'Normal'
        # Log
        extracted = {'sender': sender, 'intent': intent, 'urgency': urgency}
        self.memory.log(source='EmailAgent', type_='Email', extracted_values=str(extracted), thread_id=None)
        return extracted
