import pytest
from hardpy import DialogBox, run_dialog_box
from hardpy.pytest_hardpy.utils.dialog_box import ImageComponent

pytestmark = pytest.mark.module_name("Base dialog box")


@pytest.mark.case_name("Empty test before")
def test_before():
    assert True


@pytest.mark.case_name("Base \n dialog box with image")
def test_base_dialog_box_with_image():
    dbx = DialogBox(
        title_bar="Operator \n check",
        dialog_text="Press \n the Confirm button",
        image=ImageComponent(address="assets/test_1.png", width=100, border=1),
    )
    response = run_dialog_box(dbx)
    assert response


@pytest.mark.case_name("Base dialog box")
def test_base_dialog_box():
    dbx = DialogBox(
        title_bar="Operator check",
        dialog_text="Press the Confirm button",
    )
    response = run_dialog_box(dbx)
    assert response


@pytest.mark.case_name("Empty test after")
def test_after():
    assert True
