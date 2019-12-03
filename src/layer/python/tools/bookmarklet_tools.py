from base64 import urlsafe_b64encode
from typing import Optional

SUCCESS = "Success"
FAILED = "Failed"


def get_raw_encoded_article(event) -> Optional[str]:
    try:
        return event["queryStringParameters"]["Article"]
    except Exception:
        return None


def get_raw_encoded_config(event) -> Optional[str]:
    try:
        return event["queryStringParameters"]["Config"]
    except Exception:
        return None


def get_raw_encoded_message(event) -> Optional[str]:
    try:
        return event["queryStringParameters"]["Message"]
    except Exception:
        return None


def is_success(event) -> bool:
    try:
        status = event["queryStringParameters"]["Status"]
        return status == SUCCESS
    except Exception:
        return False


def create_failed_response(message: str, raw_encoded_article: Optional[str] = None):
    encoded_message = urlsafe_b64encode(message.encode()).decode()
    location = f"result?Status={FAILED}&Message={encoded_message}"
    if raw_encoded_article is not None:
        location += f"&Article={raw_encoded_article}"
    return {"statusCode": 303, "headers": {"Location": location}}


def create_success_response(raw_encoded_article: str):
    return {
        "statusCode": 303,
        "headers": {
            "Location": f"result?Status={SUCCESS}&Article={raw_encoded_article}"
        },
    }
