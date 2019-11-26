from .json import dumps


def create_response(status_code: int, body: dict, **headers) -> dict:
    base_header = {"Content-Type": "application/json"}
    return {
        "statusCode": status_code,
        "headers": {**base_header, **headers},
        "body": dumps(body),
    }
