import os


def get_custom_environment_values(*args) -> dict:
    result = {}
    for key in [
        "AWS_ENV",  # 環境の識別子。prodとかdevとか。
        "BOOKMARKS_USER_ID",  # ユーザーID (シングルユーザーの個人用だから必要ないと言えばないんだけど一応)
    ] + list(args):
        result[key] = os.environ.get(key)
    return result


def get_environ() -> str:
    return os.environ["AWS_ENV"]


def get_articles_table_name() -> str:
    return os.environ["ARTICLES_TABLE_NAME"]


def get_kms_key_id() -> str:
    return os.environ["KMS_KEY_ID"]


def get_user_id() -> str:
    return os.environ["BOOKMARKS_USER_ID"]
