import json


class Article(object):
    def __init__(self, url: str, title: str):
        self.url = url
        self.title = title

    def to_json(self):
        return json.dumps({"url": self.url, "title": self.title}, ensure_ascii=False)

    @classmethod
    def loads(cls, text: str):
        """
        :param text: JSON Text
        :return:  Article
        """
        data = json.loads(text)
        if not isinstance(data, dict):
            raise TypeError("invalid format (article document)")
        url = data.get("url")
        if not isinstance(url, str):
            raise TypeError("invalid format (article url)")
        title = data.get("title")
        if not isinstance(title, str):
            raise TypeError("invalid format (article title)")
        if len(title) == 0:
            title = url
        return Article(url, title)
