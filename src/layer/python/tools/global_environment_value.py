import os


def get_env() -> str:
    return os.environ['AWS_ENV']


def get_articles_table_name() -> str:
    return os.environ['ARTICLES_TABLE_NAME']


def get_kms_key_id() -> str:
    return os.environ['KMS_KEY_ID']


def get_user_id() -> str:
    return os.environ['BOOKMARKS_USER_ID']
