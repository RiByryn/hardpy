import pytest

from hardpy import (
    DialogBox,
    TextInputWidget,
    run_dialog_box,
    set_message,
)

pytestmark = pytest.mark.module_name("Main tests")


@pytest.mark.case_name("Text input")
def test_text_input():
    dbx = DialogBox(
        dialog_text="Type 'ok' and press Pass or Fail button",
        title_bar="Example of text input with pass/fail",
        widget=TextInputWidget(),
        font_size=18,
    )
    response = run_dialog_box(dbx)
    set_message(f" Entered text: {response}")
    assert response == "ok", "The entered text is not correct"
