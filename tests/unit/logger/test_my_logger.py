import json
from uuid import uuid4

import pytest
from _pytest.capture import CaptureFixture
from freezegun import freeze_time

from logger.my_logger import MyLogger


class TestDebug(object):
    @pytest.mark.parametrize(
        "name, msg, args, kwargs",
        [
            (str(uuid4()), str(uuid4()), [], {}),
            (
                str(uuid4()),
                str(uuid4()),
                [str(uuid4()), str(uuid4()), str(uuid4())],
                {str(uuid4()): str(uuid4()), str(uuid4()): str(uuid4())},
            ),
        ],
    )
    @freeze_time("2019/06/06 02:34:23.541000+00:00")  # 1559788463541
    def test_normal(self, capfd: CaptureFixture, name, msg, args, kwargs):
        MyLogger(name).debug(msg, *args, **kwargs)

        _, err = capfd.readouterr()
        actual = json.loads(err)

        assert actual["name"] == name
        assert actual["msg"] == msg
        assert actual["args"] == args
        assert actual["levelname"] == "DEBUG"
        assert actual["additional_data"] == kwargs


class TestInfo(object):
    @pytest.mark.parametrize(
        "name, msg, args, kwargs",
        [
            (str(uuid4()), str(uuid4()), [], {}),
            (
                str(uuid4()),
                str(uuid4()),
                [str(uuid4()), str(uuid4()), str(uuid4())],
                {str(uuid4()): str(uuid4()), str(uuid4()): str(uuid4())},
            ),
        ],
    )
    @freeze_time("2019/06/06 02:34:23.541000+00:00")  # 1559788463541
    def test_normal(self, capfd: CaptureFixture, name, msg, args, kwargs):
        MyLogger(name).info(msg, *args, **kwargs)

        _, err = capfd.readouterr()
        actual = json.loads(err)

        assert actual["name"] == name
        assert actual["msg"] == msg
        assert actual["args"] == args
        assert actual["levelname"] == "INFO"
        assert actual["additional_data"] == kwargs


class TestWarning(object):
    @pytest.mark.parametrize(
        "name, msg, args, kwargs",
        [
            (str(uuid4()), str(uuid4()), [], {}),
            (
                str(uuid4()),
                str(uuid4()),
                [str(uuid4()), str(uuid4()), str(uuid4())],
                {str(uuid4()): str(uuid4()), str(uuid4()): str(uuid4())},
            ),
        ],
    )
    @freeze_time("2019/06/06 02:34:23.541000+00:00")  # 1559788463541
    def test_normal(self, capfd: CaptureFixture, name, msg, args, kwargs):
        MyLogger(name).warning(msg, *args, **kwargs)

        _, err = capfd.readouterr()
        actual = json.loads(err)

        assert actual["name"] == name
        assert actual["msg"] == msg
        assert actual["args"] == args
        assert actual["levelname"] == "WARNING"
        assert actual["additional_data"] == kwargs


class TestError(object):
    @pytest.mark.parametrize(
        "name, msg, args, kwargs",
        [
            (str(uuid4()), str(uuid4()), [], {}),
            (
                str(uuid4()),
                str(uuid4()),
                [str(uuid4()), str(uuid4()), str(uuid4())],
                {str(uuid4()): str(uuid4()), str(uuid4()): str(uuid4())},
            ),
        ],
    )
    @freeze_time("2019/06/06 02:34:23.541000+00:00")  # 1559788463541
    def test_normal(self, capfd: CaptureFixture, name, msg, args, kwargs):
        MyLogger(name).error(msg, *args, **kwargs)

        _, err = capfd.readouterr()
        actual = json.loads(err)

        assert actual["name"] == name
        assert actual["msg"] == msg
        assert actual["args"] == args
        assert actual["levelname"] == "ERROR"
        assert actual["additional_data"] == kwargs
