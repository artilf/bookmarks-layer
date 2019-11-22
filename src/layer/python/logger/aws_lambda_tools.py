import os
from functools import wraps
from .my_logger import create_logger
from .define import LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME

logger = create_logger(__name__)


def save_lambda_request_id(lambda_handler):
    @wraps(lambda_handler)
    def save_lambda_request_id_to_environ(event, context):
        try:
            os.environ[LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME] = context.aws_request_id
        except Exception as e:
            logger.warning(f'Exception occurred: {e}', exc_info=True)
        return lambda_handler(event, context)
    return save_lambda_request_id_to_environ
