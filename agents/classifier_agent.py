import json
from shared_memory import SharedMemory
from pdf_utils import is_pdf, extract_pdf_text
from intent_detection import detect_intent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent

class ClassifierAgent:
    def __init__(self, memory: SharedMemory):
        self.memory = memory
        self.json_agent = JSONAgent(memory)
        self.email_agent = EmailAgent(memory)

    def classify(self, input_data):
        # Detect format
        if isinstance(input_data, dict):
            fmt = 'JSON'
        elif is_pdf(input_data):
            fmt = 'PDF'
        elif isinstance(input_data, str):
            fmt = 'Email'
        else:
            fmt = 'Unknown'
        # Detect intent
        if fmt == 'PDF':
            text = extract_pdf_text(input_data)
        elif fmt == 'JSON':
            text = json.dumps(input_data)
        else:
            text = input_data
        intent = detect_intent(text)
        # Log
        self.memory.log(source='input', type_=fmt, extracted_values=f'intent:{intent}', thread_id=None)
        return {'format': fmt, 'intent': intent}

    def route(self, input_data):
        result = self.classify(input_data)
        fmt = result['format']
        if fmt == 'JSON':
            return self.json_agent.process(input_data)
        elif fmt == 'Email':
            return self.email_agent.process(input_data)
        elif fmt == 'PDF':
            return {'pdf_text': extract_pdf_text(input_data)}
        else:
            return {'error': 'Unknown format'}
