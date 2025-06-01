import sys
import json
from agents.classifier_agent import ClassifierAgent
from shared_memory import SharedMemory

def main():
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)

    if len(sys.argv) > 1:
        input_arg = sys.argv[1]
        try:
            input_data = json.loads(input_arg)
        except Exception:
            input_data = input_arg
    else:
        input_data = input('Paste input (JSON, Email text, or PDF path): ')
        try:
            input_data = json.loads(input_data)
        except Exception:
            pass

    result = classifier.classify(input_data)
    fmt, intent = result['format'], result['intent']
    print(f"Classified as: {fmt} + {intent}")
    routed = classifier.route(input_data)
    print('Agent Output:', routed)

if __name__ == '__main__':
    main()
