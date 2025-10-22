import pytest

from hardpy import CouchdbLoader, CouchdbConfig, get_current_report

pytestmark = pytest.mark.critical  # Все тесты критичные по умолчанию

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Сохранение результатов в CouchDB и StandCloud"""
    report = get_current_report()
    if report:
        loader = CouchdbLoader(CouchdbConfig())
        loader.load(report)
    # Дополнительно в StandCloud (если настроено)
    # stand_cloud_sender.send_report()