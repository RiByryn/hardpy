import pytest
from hardpy import (
    DialogBox,
    ImageComponent,
    NumericInputWidget,
    TextInputWidget,
    run_dialog_box,
    set_message,
)

pytestmark = pytest.mark.module_name("User Input and Authentication Dialog Validation")


@pytest.mark.case_name("User authentication with security code")
def test_user_authentication():
    """Test user authentication dialog requiring security code input"""
    dbx = DialogBox(
        dialog_text="Please enter security code 'AUTH-2024' and press Confirm",
        title_bar="System Authentication Required",
        widget=TextInputWidget(),
        font_size=16,
    )
    response = run_dialog_box(dbx)
    set_message(f"User entered authentication code: {response}")
    assert response == "AUTH-2024", f"Invalid authentication code: {response}"
