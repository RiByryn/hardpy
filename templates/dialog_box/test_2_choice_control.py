import pytest
from hardpy import (
    CheckboxWidget,
    DialogBox,
    RadiobuttonWidget,
    run_dialog_box,
    set_message,
)

pytestmark = pytest.mark.module_name("System Configuration and Feature Selection Interface Testing")


@pytest.mark.case_name("System features activation")
def test_features_activation():
    """Test checkbox selection for enabling system features"""
    dbx = DialogBox(
        dialog_text='Enable "Data Logging" and "Remote Access" features, then click Confirm',
        title_bar="System Features Configuration",
        widget=CheckboxWidget(
            fields=["Data Logging", "Remote Access", "Alarm System", "Maintenance Mode"]
        ),
    )
    response = run_dialog_box(dbx)
    set_message(f"Activated features: {response}")
    expected_features = {"Data Logging", "Remote Access"}
    assert (
        set(response) == expected_features
    ), f"Feature activation mismatch: {response}"
