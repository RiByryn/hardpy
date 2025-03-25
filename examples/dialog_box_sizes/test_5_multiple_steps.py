import pytest
from hardpy import (
    DialogBox,
    ImageComponent,
    MultistepWidget,
    StepWidget,
    run_dialog_box,
)

pytestmark = pytest.mark.module_name("Multiple steps dialog box")


def test_small_100_short_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step.",
        ),
        StepWidget(
            "Step 2",
            text="Content for step.",
            image=ImageComponent(address="assets/test_6.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_small_100():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step.",
        ),
        StepWidget(
            "Step 2",
            text="Content for step.",
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_100_long_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_100():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. ",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. ",
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_small_20_long_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/test.png", width=20),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=20),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_small_20():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step.",
        ),
        StepWidget(
            "Step 2",
            text="Content for step.",
            image=ImageComponent(address="assets/test.png", width=20),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=20),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_20_long_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=20),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=20),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_20_mixed():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. ",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=20),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=20),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_small_200_long_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/test.png", width=200),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=200),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_small_200():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step.",
        ),
        StepWidget(
            "Step 2",
            text="Content for step.",
            image=ImageComponent(address="assets/test.png", width=200),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=200),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_200_long_text():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=200),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=200),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_big_200_mixed():
    steps = [
        StepWidget(
            "Step 1",
            text="Content for step. ",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=200),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=200),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_multiple_steps_different_images():
    steps = [
        StepWidget("Step 1", text="AAA"),
        StepWidget(
            "Step 2",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
    ]
    dbx = DialogBox(dialog_text="BBB", widget=MultistepWidget(steps))
    response = run_dialog_box(dbx)
    assert response


def test_multiple_steps_different_images_in_other_order():
    steps = [
        StepWidget("Step 1", text="AAA"),
        StepWidget(
            "Step 2",
            text="AAA",
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
    ]
    dbx = DialogBox(dialog_text="BBB", widget=MultistepWidget(steps))
    response = run_dialog_box(dbx)
    assert response


def test_multiple_steps_different_images_different_percent():
    steps = [
        StepWidget("Step 1", text="AAA"),
        StepWidget(
            "Step 2",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=50),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/sample_1920x1280.gif", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="BBB                                                                                                                              ",  # noqa: E501
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_multiple_steps_different_percent():
    steps = [
        StepWidget(
            "Step 1",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=20),
        ),
        StepWidget(
            "Step 2",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=50),
        ),
        StepWidget(
            "Step 3",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 4",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=150),
        ),
        StepWidget(
            "Step 5",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=200),
        ),
    ]
    dbx = DialogBox(dialog_text="BBB", widget=MultistepWidget(steps))
    response = run_dialog_box(dbx)
    assert response


def test_multiple_steps_different_percent_recursion():
    steps = [
        StepWidget(
            "Step 1",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=200),
        ),
        StepWidget(
            "Step 2",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=150),
        ),
        StepWidget(
            "Step 3",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 4",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=50),
        ),
        StepWidget(
            "Step 5",
            text="AAA",
            image=ImageComponent(address="assets/test.png", width=20),
        ),
    ]
    dbx = DialogBox(dialog_text="BBB", widget=MultistepWidget(steps))
    response = run_dialog_box(dbx)
    assert response


def test_small_100_long_text_with_line_break():
    steps = [
        StepWidget(
            "Step 1",
            text="""Some text.
            - Point 1
            - Point 2""",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_horizontal_and_vertical_stripes():
    steps = [
        StepWidget(
            "Step 1",
            text="""Some text.
            - Point 1
            - Point 2""",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/horizontal_stripe.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/vertical_stripe.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_vertical_and_horizontal_stripes():
    steps = [
        StepWidget(
            "Step 1",
            text="""Some text.
            - Point 1
            - Point 2""",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/horizontal_stripe.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/vertical_stripe.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_vertical_and_horizontal_stripes_with_small():
    steps = [
        StepWidget(
            "Step 1",
            text="""Some text.
            - Point 1
            - Point 2""",
        ),
        StepWidget(
            "Step 2",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/vertical_stripe.png", width=100),
        ),
        StepWidget(
            "Step 3",
            text=None,
            image=ImageComponent(address="assets/horizontal_stripe.png", width=100),
        ),
        StepWidget(
            "Step 4",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response


def test_vertical_and_horizontal_stripes_with_small_before_big():
    steps = [
        StepWidget(
            "Step 1",
            text=None,
            image=ImageComponent(address="assets/test.png", width=100),
        ),
        StepWidget(
            "Step 2",
            text="""Some text.
            - Point 1
            - Point 2""",
        ),
        StepWidget(
            "Step 3",
            text="Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. Content for step. ",  # noqa: E501
            image=ImageComponent(address="assets/vertical_stripe.png", width=100),
        ),
        StepWidget(
            "Step 4",
            text=None,
            image=ImageComponent(address="assets/horizontal_stripe.png", width=100),
        ),
    ]
    dbx = DialogBox(
        dialog_text="Follow the steps and click Confirm",
        widget=MultistepWidget(steps),
    )
    response = run_dialog_box(dbx)
    assert response
