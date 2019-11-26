from typing import List
import json


class PostedConfig(object):
    def __init__(self, tags: List[str]):
        def validate_tags(tags: List[str]):
            if not isinstance(tags, list):
                raise TypeError(f'tags is not list. ([{type(tags)}] {tags})')
            for i, key in enumerate(tags):
                if not isinstance(key, str):
                    raise TypeError(f'tags[{i}] is not string. ([{type(key)}] {key})')
                if len(key) == 0:
                    raise ValueError(f'tags[{i}] is empty string.')
        validate_tags(tags)
        self.tags = set(tags)

    def to_json(self) -> str:
        def default(obj):
            if isinstance(obj, set):
                return list(obj)
            return obj
        return json.dumps({'tags': self.tags}, default=default)
