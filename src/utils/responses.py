from aws_lambda_powertools.event_handler import Response, content_types
import json

def api_success(status_code, response_time, headers, body):
    return Response(
        status_code=status_code,
        content_type=content_types.APPLICATION_JSON,
        headers=headers,
        body=json.dumps(body)
    )

def api_error(status_code, response_time, headers, reason_failure, msg):
    return Response(
        status_code=status_code,
        content_type=content_types.APPLICATION_JSON,
        headers=headers,
        body=json.dumps({
            "failure": reason_failure,
            "msg": msg
        })
    )