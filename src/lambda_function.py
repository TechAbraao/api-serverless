import json

def lambda_handler(event, context):
    
    method = event.get("httpMethod", "GET")
    path_params = event.get("pathParameters") or {}
    query_params = event.get("queryStringParameters") or {}
    headers = event.get("headers") or {}
    
    user_id = path_params.get("id")
    
    auth_header = headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return {
            "statusCode": 401,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"erro": "Invalid token."})
        }
    
    body = {}
    if event.get("body"):
        body = json.loads(event["body"])
    
    resposta = {
        "user_id": user_id,
        "active_filter": query_params.get("ativo"),
        "data": body,
        "method": method
    }
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "responseTime": None,
        "body": json.dumps(resposta)
    }