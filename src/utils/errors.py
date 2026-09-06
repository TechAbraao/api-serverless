from enum import Enum

class ReasonFailure(str, Enum):
    """
    Padronização dos códigos de motivo de falha (reason_failure / error codes).
    """

    INVALID_AUTH_HEADER = "INVALID_AUTH_HEADER"
    MISSING_AUTH_HEADER = "MISSING_AUTH_HEADER"
    INVALID_TOKEN = "INVALID_TOKEN"
    EXPIRED_TOKEN = "EXPIRED_TOKEN"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"

    BAD_REQUEST = "BAD_REQUEST"
    INVALID_PAYLOAD = "INVALID_PAYLOAD"
    MISSING_REQUIRED_FIELDS = "MISSING_REQUIRED_FIELDS"
    INVALID_QUERY_PARAMS = "INVALID_QUERY_PARAMS"

    NOT_FOUND = "NOT_FOUND"
    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"

DEFAULT_ERROR_MESSAGES = {
    ReasonFailure.INVALID_AUTH_HEADER: "Authorization header is required and must start with 'Bearer '",
    ReasonFailure.MISSING_AUTH_HEADER: "Authorization header is missing",
    ReasonFailure.INVALID_TOKEN: "The provided token is invalid or corrupted",
    ReasonFailure.EXPIRED_TOKEN: "The provided token has expired",
    ReasonFailure.UNAUTHORIZED: "Unauthorized access",
    ReasonFailure.FORBIDDEN: "You do not have permission to access this resource",
    ReasonFailure.BAD_REQUEST: "The request payload or parameters are invalid",
    ReasonFailure.INVALID_PAYLOAD: "The request body contains invalid data",
    ReasonFailure.MISSING_REQUIRED_FIELDS: "Required fields are missing in the request body",
    ReasonFailure.INVALID_QUERY_PARAMS: "Invalid query parameters provided",
    ReasonFailure.NOT_FOUND: "The requested resource was not found",
    ReasonFailure.RESOURCE_ALREADY_EXISTS: "Resource already exists",
    ReasonFailure.INTERNAL_SERVER_ERROR: "An unexpected internal server error occurred",
    ReasonFailure.DATABASE_ERROR: "An error occurred while interacting with the database",
}
