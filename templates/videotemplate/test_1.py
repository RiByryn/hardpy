import random
from datetime import datetime

import pytest

from hardpy import (
    Chart,
    ChartType,
    CheckboxWidget,
    ComparisonOperation as CompOp,
    DialogBox,
    NumericInputWidget,
    NumericMeasurement,
    RadiobuttonWidget,
    run_dialog_box,
    set_case_chart,
    set_case_measurement,
    set_message,
    set_operator_message,
)
from hardpy.pytest_hardpy.utils.const import Group

pytestmark = pytest.mark.module_name("Hardpy example")

@pytest.mark.case_group(Group.SETUP)
def test_initialize_system():
    """System initialization - critical test."""
    set_message("Starting system initialization", "init_start")

    dialog = DialogBox(
        dialog_text="Connect temperature controller to 220V power supply",
        title_bar="Test stand setup",
        widget=CheckboxWidget(fields=["Ready", "Not ready"]),
    )
    response = run_dialog_box(dialog)
    set_message(f"Response: {response}", "operator_response")

    expected_response = ["Ready"]
    assert response == expected_response, "Operator did not confirm connection"

    set_message("System initialized successfully", "init_success")


@pytest.mark.case_group(Group.SETUP)
@pytest.mark.dependency(depends=["test_initialize_system"])
def test_check_communication():
    """Check communication with controller."""
    set_operator_message(
        "Checking equipment communication...", title="Communication check", block=False
    )
    # Simulate communication check
    comm_status = random.choice([True, True, True, False])  # 75% success rate
    if comm_status:
        set_message("Communication with controller established", "comm_ok")
    else:
        set_message("Communication error with controller", "comm_fail")
    assert comm_status, "Communication error with controller"


@pytest.mark.case_group(Group.MAIN)
@pytest.mark.dependency(depends=["test_check_communication"])
@pytest.mark.attempt(3)  # 3 attempts on failure
def test_temperature_measurement():
    """Temperature measurement with multiple attempts."""
    # Simulate temperature measurements
    temperatures = [round(random.uniform(20.0, 25.0), 2) for _ in range(5)]

    # Create measurements with correct comparisons
    meas0 = NumericMeasurement(value=temperatures[0])
    set_case_measurement(meas0)
    set_message(f"First measurement: {meas0.value}°C")

    # Measurement that should pass successfully
    target_temp = 22.5
    current_temp = round(random.uniform(22.0, 23.0), 2)  # Value close to target
    meas1 = NumericMeasurement(
        value=current_temp,
        operation=CompOp.EQ,
        comparison_value=target_temp,
    )
    set_case_measurement(meas1)
    set_message(f"Current temperature: {current_temp}°C, target: {target_temp}°C")

    # Another measurement
    meas2 = NumericMeasurement(
        value=23.0,
        operation=CompOp.LE,  # Less than or equal
        comparison_value=25.0,
    )
    set_case_measurement(meas2)

    # Create temperature chart - FIXED according to documentation
    timestamps = [
        float(i) for i in range(len(temperatures))
    ]  # Explicit conversion to float
    chart = Chart(
        type=ChartType.LINE,
        title="Temperature Changes",
        x_label="Time, s",
        y_label="Temperature, °C",
        marker_name=["Temperature", "Target"],  # Two markers for two data series
        x_data=[timestamps, timestamps],  # X data for both series
        y_data=[
            temperatures,
            [target_temp] * len(temperatures),
        ],  # Actual and target temperatures
    )
    set_case_chart(chart)

    avg_temp = sum(temperatures) / len(temperatures)
    set_message(f"Average temperature: {avg_temp:.2f}°C", "avg_temp")

    # Check measurement results
    assert (
        meas1.result
    ), f"Temperature {current_temp}°C does not match target {target_temp}°C"
    assert meas2.result, "Temperature exceeds allowable limit"

    # Simulate random failure (for demo attempts) - reduced probability
    if random.random() < 0.2:  # 20% failure probability instead of 30%
        assert False, "Random measurement error"


@pytest.mark.case_group(Group.MAIN)
def test_temperature_validation():
    """Temperature regime validation."""
    dialog = DialogBox(
        dialog_text="Set temperature to 100°C on the controller",
        title_bar="Calibration",
        widget=RadiobuttonWidget(fields=["Completed", "Skip", "Abort"]),
    )
    response = run_dialog_box(dialog)

    if response == "Skip":
        pytest.skip("Calibration skipped by operator")
    elif response == "Abort":
        assert False, "Test aborted by operator"

    # Simulate temperature reading
    current_temp = random.uniform(95.0, 105.0)
    set_message(f"Current temperature: {current_temp:.2f}°C", "calibration_temp")

    assert 98.0 <= current_temp <= 102.0, f"Temperature {current_temp}°C out of range"


@pytest.mark.case_group(Group.MAIN)
@pytest.mark.dependency(depends=["test_temperature_validation"])
def test_advanced_controls():
    """Advanced controls with HTML content."""
    set_operator_message(
        msg="Additional functions check\n\n"
        "• Check LED indicators\n"
        "• Verify fan operation\n"
        "• Check LCD display",
        title="Extended verification",
        block=True,
    )

    # Numeric input from operator
    dialog = DialogBox(
        dialog_text="Enter number of successful checks (1-3):",
        title_bar="Verification results",
        widget=NumericInputWidget(),  # Fixed widget name
    )
    checks_passed = run_dialog_box(dialog)
    set_message(f"Successfully passed {checks_passed}/3 checks", "advanced_checks")
    assert checks_passed >= 2, f"Failed {3 - checks_passed} checks"


@pytest.mark.case_group(Group.TEARDOWN)
def test_system_shutdown():
    """Correct system shutdown."""
    set_message("Starting shutdown procedure", "shutdown_start")

    dialog = DialogBox(
        dialog_text="Disconnect temperature controller power supply",
        title_bar="Shutdown",
        widget=CheckboxWidget(fields=["Power disconnected", "Save logs"]),
    )
    response = run_dialog_box(dialog)
    set_message(f"Operator response: {response}", "shutdown_response")

    # Check that at least "Power disconnected" is selected
    assert (
        "Power disconnected" in response
    ), "Operator did not confirm power disconnection"

    set_message("System shutdown completed", "shutdown_complete")
