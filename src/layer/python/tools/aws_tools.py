import os
from logger.define import LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
from logger.my_logger import MyLogger
from functools import wraps
from .global_environment_value import get_custom_environment_values

logger = MyLogger(__name__)


def save_lambda_request_id(lambda_handler):
    @wraps(lambda_handler)
    def save_lambda_request_id_to_environ(event, context):
        logger.info('event and custom environment values', event=event, environ=get_custom_environment_values())
        try:
            os.environ[
                LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
            ] = context.aws_request_id
        except Exception as e:
            logger.warning(f"Exception occurred: {e}")
        return lambda_handler(event, context)

    return save_lambda_request_id_to_environ
