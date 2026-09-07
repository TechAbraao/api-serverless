from aws_lambda_powertools.event_handler import Request
from aws_lambda_powertools import Logger
from src.utils.responses import api_success, api_error
from src.utils.errors import ReasonFailure, DEFAULT_ERROR_MESSAGES
from src.utils.mocks import TOKEN_JWT, CONTACTS
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
    logger.info("Fetching GET /api/contacts endpoint.")

    if (not authorization_header) or (not authorization_header.startswith("Bearer ")):
        end = time.time()
        response_time_ms = (end - start) * 1000

        logger.error("Missing or invalid Authorization header.")
        return api_error(
                status_code=500,
                response_time=response_time_ms,
                headers={
                    "Content-Type": content_type_header ,
                    "Authorization": authorization_header
                },
                reason_failure=ReasonFailure.INVALID_AUTH_HEADER,
                msg=DEFAULT_ERROR_MESSAGES[ReasonFailure.INVALID_AUTH_HEADER]
        )

    token = authorization_header[7:]
    if token != TOKEN_JWT:
        end = time.time()
        response_time_ms = (end - start) * 1000

        logger.error("Invalid token provided.")
        return api_error(
                status_code=401,
                response_time=response_time_ms,
                headers={
                    "Content-Type": content_type_header ,
                    "Authorization": authorization_header
                },
                reason_failure=ReasonFailure.INVALID_TOKEN,
                msg=DEFAULT_ERROR_MESSAGES[ReasonFailure.INVALID_TOKEN]
            )

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