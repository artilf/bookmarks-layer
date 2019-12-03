import json
from typing import List


class PostedConfig(object):
    def __init__(self, tags: List[str]):
        def validate_tags(tags: List[str]):
            if not isinstance(tags, list):
                raise TypeError(f"tags is not list. ([{type(tags)}] {tags})")
            if len(tags) == 0:
                raise ValueError(f"tags is empty list.")
            for i, key in enumerate(tags):
                if not isinstance(key, str):
                    raise TypeError(f"tags[{i}] is not string. ([{type(key)}] {key})")
                if len(key) == 0:
                    raise ValueError(f"tags[{i}] is empty string.")

        validate_tags(tags)
        self.tags = set(tags)

    def to_json(self) -> str:
        return json.dumps({"tags": list(self.tags)})

    @staticmethod
    def loads(text: str):
        data = json.loads(text)
        if not isinstance(data, dict):
            raise TypeError("invalid format (config document)")
        tags = data.get("tags")
        if tags is None:
            raise TypeError("invalid format (config tags)")
        return PostedConfig(tags)
