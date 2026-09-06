from aws_lambda_powertools.event_handler import Request
from aws_lambda_powertools import Logger
from src.mocks import TOKEN_JWT, CONTACTS
from src import app
import time

logger = Logger()

@app.get("/api/contacts")
def get_contacts(req: Request):
    start = time.time()
    end = None
    response_time_ms = None
    authorization_header = req.headers.get("Authorization")
    content_type_header = req.headers.get("Content-Type")

    # logger.info("[GET] /api/contacts")

    if (not authorization_header) or (not authorization_header.startswith("Bearer ")):
        end = time.time()
        response_time_ms = (end - start) * 1000
        return {
            "statusCode": 500,
            "responseTimeMs": response_time_ms,
            "headers": {
                "Content-Type": content_type_header ,
                "Authorization": authorization_header
            },
            "body": {
                "errorDescription": "Missing or invalid Authorization header"
            }
        }

    token = authorization_header[7:]
    if token != TOKEN_JWT:
        end = time.time()
        response_time_ms = (end - start) * 1000
        return {
            "statusCode": 401,
            "responseTimeMs": response_time_ms,
            "headers": {
                "Content-Type": content_type_header ,
                "Authorization": authorization_header
            },
            "body": {   
                "errorDescription": "Invalid Token",
            }
        }

    end = time.time()
    # Aqui é pra obter em milisegundos
    response_time_ms = (end - start) * 1000
    return {
        "statusCode": 200,
        "responseTimeMs": response_time_ms,
        "headers": {
            "Content-Type": authorization_header,
            "Authorization": content_type_header 
        },
        "body": {
            "data": CONTACTS
        }
    }

@app.post("/api/contacts")
def post_contact(req: Request):
    start = time.time()
    authorization_header = req.headers.get("Authorization")
    content_type_header = req.headers.get("Content-Type")
    

    end = time.time()
    response_time_ms = (end - start) * 1000
    return {
        "statusCode": 200,
        "responseTime": response_time_ms,
        "headers": {
            "Content-Type": authorization_header,
            "Authorization": content_type_header 
        }
    }