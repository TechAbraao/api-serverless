import json
import os
import pytest
from dataclasses import dataclass
from src.lambda_function import lambda_handler

@dataclass
class MockLambdaContext:
    function_name: str = "test-function"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:us-east-1:123456789012:function:test-function"
    aws_request_id: str = "test-request-id"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_event(filename):
    if filename.startswith("API_GATEWAY_PAYLOAD"):
        filepath = os.path.join(BASE_DIR, filename)
    else:
        filepath = os.path.join(BASE_DIR, "events", filename)
    
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def test_get_api_contacts_success():
    """
        Valida se o evento de token válido retorna os contatos com sucesso.
    """

    event = load_event("GET_API_CONTACTS_SUCCESS.json")
    context = MockLambdaContext()
    response = lambda_handler(event, context)
    
    assert response["statusCode"] == 200
    
    body = json.loads(response["body"])
    print("PRINTAQUUIIIII", body)
   
    assert "data" in body
    assert len(body["data"]) == 5
    #assert body["body"]["data"][0]["name"] == "João Silva"

def test_invalid_auth_header():
    """
        Valida se a falta ou header incorreto de Authorization retorna erro 401.
    """
    event = load_event("INVALID_AUTH_HEADER.json")
    context = MockLambdaContext()
    
    response = lambda_handler(event, context)
    
    assert response["statusCode"] == 401
    
    # body = json.loads(response["body"])
    #assert body["body"]["failure"] == "INVALID_AUTH_HEADER"
    #assert "missing or invalid" in body["body"]["msg"].lower() or "ausente" in body["body"]["msg"].lower()

def test_invalid_token():
    """
        Valida se um token diferente do esperado retorna erro 401 de token inválido.
    """

    event = load_event("INVALID_TOKEN.json")
    context = MockLambdaContext()
    
    response = lambda_handler(event, context)
    
    assert response["statusCode"] == 401
    
    #body = json.loads(response["body"])
    #assert "invalid or corrupted" in body["body"]["msg"].lower() or "inválido" in body["body"]["msg"].lower()