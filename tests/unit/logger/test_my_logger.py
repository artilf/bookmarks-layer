import json
from uuid import uuid4

import pytest
from _pytest.capture import CaptureFixture
from freezegun import freeze_time

from logger.my_logger import MyLogger


class TestDebug(object):
    @pytest.mark.parametrize(
        "name, msg, kwargs",
        [
            (str(uuid4()), str(uuid4()), {}),
            (
                str(uuid4()),
                str(uuid4()),
                {str(uuid4()): str(uuid4()), str(uuid4()): str(uuid4())},
            ),
        ],
    )
    @freeze_time("2019/06/06 02:34:23.541000+00:00")  # 1559788463541
    def test_normal(self, capfd: CaptureFixture, name, msg, kwargs):
        MyLogger(name).debug(msg, **kwargs)

        _, err = capfd.readouterr()
        actual = json.loads(err)

        assert actual["name"] == name
        assert actual["msg"] == msg
        assert actual["levelname"] == "DEBUG"
        assert actual["additional_data"] == kwargs
