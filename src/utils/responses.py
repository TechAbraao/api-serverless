
def api_success(
        status_code: int, 
        response_time: 
        float, 
        headers: dict, 
        body: dict
):
    return {
        "statusCode": status_code,
        "responseTime": response_time,
        "headers": headers,
        "body": body
    }


def api_error(
        status_code: int, 
        response_time: float,
        headers: dict, 
        reason_failure: str,
        msg: str
        ):
    return {
        "statusCode": status_code,
        "responseTime": response_time,
        "headers": headers,
        "body": {
            "failure": reason_failure,
            "msg": msg
        }
    }
   