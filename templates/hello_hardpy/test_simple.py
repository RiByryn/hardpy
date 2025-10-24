import pytest

from hardpy import Chart, ChartType, set_case_chart

pytestmark = pytest.mark.module_name("Charts")


@pytest.mark.case_name("Multiple charts")
def test_multiple_charts():
    chart = Chart()
    chart.add_series(x_data=[1, 2, 3], y_data=[1, 2, 3], marker_name="a")
    chart.add_series(x_data=[1, 2, 4], y_data=[5, 4, 3], marker_name="b")
    set_case_chart(chart)
