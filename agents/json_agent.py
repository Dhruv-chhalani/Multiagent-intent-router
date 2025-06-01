from shared_memory import SharedMemory

class JSONAgent:
    def __init__(self, memory: SharedMemory):
        self.memory = memory

    def process(self, payload):
        # Example: Extract and reformat to target schema
        target_schema = {k: payload.get(k, None) for k in ['id', 'amount', 'date', 'customer']}
        # Flag anomalies
        missing = [k for k, v in target_schema.items() if v is None]
        anomalies = {'missing_fields': missing} if missing else {}
        # Log
        self.memory.log(source='JSONAgent', type_='JSON', extracted_values=str(target_schema), thread_id=None)
        return {'data': target_schema, 'anomalies': anomalies}
