import os
import sys
from functools import wraps

import boto3
import botocore

from logger.json_log_formatter import LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
from logger.my_logger import MyLogger

from ._aws_tools import prepare_get_aws_client
from .environment_values import get_custom_environment_values

logger = MyLogger(__name__)

get_ssm_client = prepare_get_aws_client("ssm")
get_kms_client = prepare_get_aws_client("kms")


def save_lambda_request_id(*extra_environment_value_names):
    def wrapper(handler):
        @wraps(handler)
        def save_lambda_request_id_to_environ(event, context):
            try:
                os.environ[
                    LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME
                ] = context.aws_request_id
            except Exception as e:
                logger.warning(f"Exception occurred: {e}")

            try:
                logger.info(
                    "event, custom environment values, python version, and boto3 version",
                    event=event,
                    environ=get_custom_environment_values(
                        *extra_environment_value_names
                    ),
                    versions={
                        "python": sys.version,
                        "boto3": boto3.__version__,
                        "botocore": botocore.__version__,
                    },
                )
            except Exception as e:
                logger.warning(f"Exception occurred: {e}")
            return handler(event, context)

        return save_lambda_request_id_to_environ

    return wrapper
