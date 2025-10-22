import random
from datetime import datetime

import pytest

from hardpy import (
    CheckboxWidget,
    DialogBox,
    NumericInputWidget,
    RadiobuttonWidget,
    run_dialog_box,
    set_case_chart,
    set_case_measurement,
    set_message,
    set_operator_message,
)
from hardpy.pytest_hardpy.utils.const import Group


@pytest.mark.case_group(Group.SETUP)
@pytest.mark.critical
def test_initialize_system():
    """Инициализация системы - критический тест."""
    set_message("Начало инициализации системы", "init_start")

    # Диалог с оператором
    dialog = DialogBox(
        dialog_text="Подключите контроллер температуры к питанию 220V",
        title_bar="Настройка стенда",
        widget=CheckboxWidget(fields=["Готово", "Не готово"]),
    )
    response = run_dialog_box(dialog)
    set_message("Система инициализирована успешно", "init_success")
    set_message("Ответ", response)
    correct_answer = {"Готово"}
    assert set(response) == correct_answer, "Оператор не подтвердил подключение"

@pytest.mark.case_group(Group.SETUP)
@pytest.mark.dependency("test_initialize_system")
def test_check_communication():
    """Проверка связи с контроллером."""
    set_operator_message(
        "Проверка связи с оборудованием...", title="Проверка связи", block=False
    )
    # Имитация проверки связи
    comm_status = random.choice([True, True, True, False])  # 75% успеха
    set_message("Связь с контроллером установлена", "comm_ok")
    assert comm_status, "Ошибка связи с контроллером"


@pytest.mark.case_group(Group.MAIN)
@pytest.mark.dependency("test_check_communication")
@pytest.mark.attempt(3)  # 3 попытки при падении
def test_temperature_measurement():
    """Измерение температуры с несколькими попытками."""
    temperatures = [round(random.uniform(20.0, 25.0), 2) for _ in range(10)]

    # Сохранение измерений
    set_case_measurement("temperature_readings", temperatures)

    # Сохранение графика
    timestamps = list(range(10))
    chart_data = {"x": timestamps, "y": temperatures, "name": "Температура, °C"}
    set_case_chart("temperature_chart", chart_data)

    avg_temp = sum(temperatures) / len(temperatures)
    set_message(f"Средняя температура: {avg_temp:.2f}°C", "avg_temp")

    # Имитация случайного падения (для демо attempts)
    if random.random() < 0.3:  # 30% вероятность падения
        assert False, "Случайная ошибка измерения"


@pytest.mark.case_group(Group.MAIN)
def test_temperature_validation():
    """Валидация температурного режима."""
    dialog = DialogBox(
        dialog_text="Установите температуру 100°C на контроллере",
        title_bar="Калибровка",
        widget=RadiobuttonWidget(options=["Выполнено", "Пропустить", "Прервать"]),
    )
    response = run_dialog_box(dialog)

    if response == "Пропустить":
        pytest.skip("Калибровка пропущена оператором")
    elif response == "Прервать":
        assert False, "Тест прерван оператором"

    # Имитация чтения температуры
    current_temp = random.uniform(95.0, 105.0)
    set_message(f"Текущая температура: {current_temp:.2f}°C", "calibration_temp")

    assert 98.0 <= current_temp <= 102.0, f"Температура {current_temp}°C вне диапазона"


@pytest.mark.case_group(Group.MAIN)
@pytest.mark.dependency("test_temperature_validation")
def test_advanced_controls():
    """Продвинутое управление с HTML контентом."""
    set_operator_message(
        msg="""<h3>Проверка дополнительных функций</h3>
              <ul>
                <li>Проверьте светодиодные индикаторы</li>
                <li>Убедитесь в работе вентилятора</li>
                <li>Проверьте LCD дисплей</li>
              </ul>""",
        title="Расширенная проверка",
        block=True,
    )

    # Числовой ввод от оператора
    dialog = DialogBox(
        dialog_text="Введите количество успешных проверок (1-3):",
        title_bar="Результаты проверки",
        widget=NumericInputWidget(min=1, max=3, default=3),
    )
    checks_passed = run_dialog_box(dialog)
    set_message(f"Успешно пройдено {checks_passed}/3 проверок", "advanced_checks")
    assert checks_passed >= 2, f"Провалено {3 - checks_passed} проверок"


@pytest.mark.case_group(Group.TEARDOWN)
def test_system_shutdown():
    """Корректное завершение работы."""
    set_message("Начало процедуры завершения", "shutdown_start")

    dialog = DialogBox(
        dialog_text="Отключите питание контроллера температуры",
        title_bar="Завершение работы",
        widget=CheckboxWidget(options=["Питание отключено", "Сохранить логи"]),
    )
    response = run_dialog_box(dialog)

    set_message("Система завершила работу", "shutdown_complete")

    assert response
