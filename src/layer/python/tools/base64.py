from base64 import b64decode, b64encode


def urlsafe_encode(obj: str) -> str:
    encoded: str = b64encode(obj.encode()).decode()
    return encoded.replace("+", "-").replace("=", "_").replace("/", "~")


def urlsafe_decode(obj: str) -> str:
    unsafe = obj.replace("-", "+").replace("_", "=").replace("~", "/")
    decoded = b64decode(unsafe.encode()).decode()
    return decoded
