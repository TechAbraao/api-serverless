import json
from src.lambda_function import lambda_handler

with open("API_GATEWAY_PAYLOAD.json") as f:
    event = json.load(f)

context = {}

response = lambda_handler(event, context)
print(json.dumps(response, indent=2))