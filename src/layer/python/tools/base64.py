from base64 import b64decode, b64encode


def urlsafe_encode(obj: bytes) -> str:
    encoded: str = b64encode(obj).decode()
    return encoded.replace("+", "-").replace("=", "_").replace("/", "~")


def urlsafe_decode(obj: str) -> bytes:
    unsafe = obj.replace("-", "+").replace("_", "=").replace("~", "/")
    decoded = b64decode(unsafe.encode())
    return decoded
