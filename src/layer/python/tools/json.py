import json
from decimal import Decimal
from models.posted_config import PostedConfig


def dumps(obj, **kwargs):
    def default(obj):
        if isinstance(obj, PostedConfig):
            return json.loads(obj.to_json())
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Decimal):
            return int(obj) if int(obj) == obj else float(obj)
        try:
            return str(obj)
        except Exception:
            return None

    return json.dumps(obj, default=default, ensure_ascii=False, **kwargs)
