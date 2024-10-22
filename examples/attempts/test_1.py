from time import sleep

import pytest
from driver_example import DriverExample

import hardpy
from hardpy import DialogBox, TextInputWidget, run_dialog_box


@pytest.mark.attempt(5)
def test_minute_parity(driver_example: DriverExample):
    minute = driver_example.current_minute
    hardpy.set_message(f"Current minute {minute}", "current_minute")
    hardpy.set_message(
        f"Current attempt {hardpy.get_current_attempt()}",
        "updated_status",
    )
    result = minute % 2
    data = {
        "minute": minute,
    }
    hardpy.set_case_artifact(data)
    sleep(15)
    assert result == 0, f"The test failed because {minute} is odd! Try again!"


@pytest.mark.attempt(3)
def test_dialog_box():
    dbx = DialogBox(
        dialog_text="Print '123', if you want to fail attempt. Print 'ok', if you want to pass attempt. ",  # noqa: E501
        title_bar="Example of text input",
        widget=TextInputWidget(),
    )
    response = run_dialog_box(dbx)
    if response != "ok":
        dbx = DialogBox(
            dialog_text=f"Test attempt {hardpy.get_current_attempt()}",
            title_bar="Attempt message",
        )
        run_dialog_box(dbx)

    assert response == "ok", "The entered text is not correct"
