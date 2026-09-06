import json
import os
from dataclasses import dataclass
from src.lambda_function import lambda_handler


@dataclass
class MockLambdaContext:
    function_name: str = "test-function"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:us-east-1:123456789012:function:test-function"
    aws_request_id: str = "test-request-id"

with open("API_GATEWAY_PAYLOAD.json") as f:
    event = json.load(f)

context = MockLambdaContext()

response = lambda_handler(event, context)
print(json.dumps(response, indent=2))