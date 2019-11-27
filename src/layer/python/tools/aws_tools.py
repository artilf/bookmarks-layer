from ._aws_tools import prepare_get_aws_client


get_ssm_client = prepare_get_aws_client('ssm')
get_kms_client = prepare_get_aws_client('kms')