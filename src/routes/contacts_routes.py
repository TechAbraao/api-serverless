from aws_lambda_powertools.event_handler import Request
from src import app
import time


@app.get("/api/contacts")
def get_contacts(req: Request):
    start = time.time()
    authorization_header = req.headers.get("Authorization")
    content_type_header = req.headers.get("Content-Type")

    end = time.time()
    response_time_ms = (end - start) * 1000
    return {
        "statusCode": 200,
        "responseTimeMs": response_time_ms,
        "headers": {
            "Content-Type": authorization_header,
            "Authorization": content_type_header 
        },
        "body": {}
    }

@app.post("/api/contacts")
def post_contact(req: Request):

    return {
        "statusCode": 200,
        "responseTime": None,
        "headers": {},
    }