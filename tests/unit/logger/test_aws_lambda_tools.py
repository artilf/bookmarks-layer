import os
from logging import WARNING

import pytest
from _pytest.logging import LogCaptureFixture

from logger.aws_lambda_tools import save_lambda_request_id
from logger.define import LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME


class DummyContext(object):
    def __init__(self, request_id: str):
        self.aws_request_id = request_id


@pytest.fixture(scope="function")
def dummy_context(request):
    return DummyContext(request.param)


@pytest.fixture(scope="function")
def delete_environ(request):
    yield
    for key in request.param:
        if key in os.environ:
            del os.environ[key]


@save_lambda_request_id
def dummy_func(event, context):
    pass


@pytest.mark.parametrize("delete_environ", [(["LAMBDA_REQUEST_ID"])], indirect=True)
@pytest.mark.usefixtures("delete_environ")
class TestSaveLambdaRequestId(object):
    def test_exception(self, caplog: LogCaptureFixture):
        caplog.set_level(WARNING)
        dummy_func(None, None)
        assert os.getenv(LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME) is None
        assert len(caplog.record_tuples) == 1
        log = caplog.record_tuples[0]
        assert "aws_lambda_tools" in log[0]
        assert log[1] == WARNING
        assert "Exception occurred:" in log[2]

    @pytest.mark.parametrize(
        "dummy_context, expected",
        [
            (
                "3A561BF0-0F1E-4A0E-A197-5F17A73A28FD",
                "3A561BF0-0F1E-4A0E-A197-5F17A73A28FD",
            ),
            (
                "C135EDBA-FAA9-4F32-A0CA-7EBEDF30D5D6",
                "C135EDBA-FAA9-4F32-A0CA-7EBEDF30D5D6",
            ),
        ],
        indirect=["dummy_context"],
    )
    def test_normal(self, dummy_context, expected):
        dummy_func(None, dummy_context)
        actual = os.getenv(LAMBDA_REQUEST_ID_ENVIRONMENT_VALUE_NAME)
        assert actual == expected
