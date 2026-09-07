from src.utils.responses import api_error
from src.utils.errors import ReasonFailure, DEFAULT_ERROR_MESSAGES
from src.utils.mocks import TOKEN_JWT
from aws_lambda_powertools.event_handler.exceptions import UnauthorizedError
from src import app
from aws_lambda_powertools import Logger
from functools import wraps

logger = Logger()

def api_permissions(strategy="jwt"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if strategy == "jwt":
                headers = getattr(app.current_event, "headers", {}) or {}
                headers_lower = {k.lower(): v for k, v in headers.items()}
                auth_header = headers_lower.get("authorization", "")

                if not auth_header or not auth_header.startswith("Bearer "):
                    logger.error("Missing or invalid Authorization header.")
                    raise UnauthorizedError(DEFAULT_ERROR_MESSAGES[ReasonFailure.INVALID_AUTH_HEADER])

                token = auth_header[7:]
                if token != TOKEN_JWT:
                    raise UnauthorizedError(DEFAULT_ERROR_MESSAGES[ReasonFailure.INVALID_TOKEN])
            else:
                raise ValueError(f"Unsupported strategy: {strategy}")

            return func(*args, **kwargs)
        return wrapper
    return decorator