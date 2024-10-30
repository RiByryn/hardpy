import pytest

from hardpy import DialogBox, ImageWidget, MultistepWidget, StepWidget, run_dialog_box

pytestmark = pytest.mark.module_name("Multiple steps dialog box")


@pytest.mark.case_name("Multistep")
def test_multiple_steps_1():
    img_widget = ImageWidget(address="assets/test.png", width=100)
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            widget=None,
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            widget=img_widget,
        ),
        StepWidget("Step 3", text=None, widget=img_widget),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


@pytest.mark.case_name("Multistep")
def test_multiple_steps_2():
    img_widget = ImageWidget(address="assets/test.png", width=100)
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step.",  # noqa: E501
            widget=None,
        ),
        StepWidget(
            "Step 2",
            text="Content for step.",  # noqa: E501
            widget=img_widget,
        ),
        StepWidget("Step 3", text=None, widget=img_widget),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


@pytest.mark.case_name("Multistep")
def test_multiple_steps_3():
    img_widget = ImageWidget(address="assets/sample_1920x1280.gif", width=100)
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            widget=None,
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            widget=img_widget,
        ),
        StepWidget("Step 3", text=None, widget=img_widget),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


@pytest.mark.case_name("Multistep")
def test_multiple_steps_4():
    img_widget = ImageWidget(address="assets/sample_1920x1280.gif", width=100)
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. ",  # noqa: E501
            widget=None,
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            widget=img_widget,
        ),
        StepWidget("Step 3", text=None, widget=img_widget),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response
