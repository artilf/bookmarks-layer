import os
from functools import wraps

from logger.json_log_formatter import LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
from logger.my_logger import MyLogger

from ._aws_tools import prepare_get_aws_client
from .environment_values import get_custom_environment_values

logger = MyLogger(__name__)

get_ssm_client = prepare_get_aws_client("ssm")
get_kms_client = prepare_get_aws_client("kms")


def save_lambda_request_id(lambda_handler):
    @wraps(lambda_handler)
    def save_lambda_request_id_to_environ(event, context):
        logger.info(
            "event and custom environment values",
            event=event,
            environ=get_custom_environment_values(),
        )
        try:
            os.environ[
                LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
            ] = context.aws_request_id
        except Exception as e:
            logger.warning(f"Exception occurred: {e}")
        return lambda_handler(event, context)

    return save_lambda_request_id_to_environ
