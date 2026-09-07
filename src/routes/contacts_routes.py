from aws_lambda_powertools.event_handler import Request
from aws_lambda_powertools import Logger
from src.utils.responses import api_success
from src.utils.mocks import CONTACTS
from src.middlewares.authorizations import api_permissions
from src import app
import time

logger = Logger()

@app.get("/api/contacts")
@api_permissions(strategy="jwt")
def get_contacts(req: Request):
    start = time.time()
    authorization_header = req.headers.get("Authorization")
    content_type_header = req.headers.get("Content-Type")
    logger.info("Fetching GET /api/contacts endpoint.")

    end = time.time()
    response_time_ms = (end - start) * 1000
    logger.info("Successfully fetched contacts.")

    return api_success(
        status_code=200,
        response_time=response_time_ms,
        headers={
            "Content-Type": content_type_header,
            "Authorization": authorization_header
        },
        body={
            "data": CONTACTS
        }
    )

@app.post("/api/contacts")
@api_permissions(strategy="jwt")
def post_contact(req: Request):
    start = time.time()
    authorization_header = req.headers.get("Authorization")
    content_type_header = req.headers.get("Content-Type")
    logger.info("Fetching POST /api/contacts endpoint.")

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