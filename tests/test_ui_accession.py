import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDate
from app.main import MainWindow
from py.xml import html

@pytest.fixture
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    main_window = MainWindow()
    return main_window


def test_initial_state(app):
    ui = app.ui
    assert ui.stackedWidget.currentIndex() == 0
    assert ui.pushButtonGotoSessions.text() == "Sessions"
    assert ui.pushButtonGotoMeasures.text() == "Statistical measures"
    assert ui.pushButtonGotoDistribution.text() == "Change distribution"


def test_goto_sessions(app):
    ui = app.ui
    ui.pushButtonGotoSessions.click()
    assert ui.stackedWidget.currentIndex() == 2


def test_goto_measures(app):
    ui = app.ui
    ui.pushButtonGotoMeasures.click()
    assert ui.stackedWidget.currentIndex() == 3


def test_goto_distribution(app):
    ui = app.ui
    ui.pushButtonGotoDistribution.click()
    assert ui.stackedWidget.currentIndex() == 1


def test_back_to_main_from_distribution(app):
    ui = app.ui
    ui.pushButtonGotoDistribution.click()
    ui.pushButtonBackToMain3.click()
    assert ui.stackedWidget.currentIndex() == 0


def test_back_to_main_from_measures(app):
    ui = app.ui
    ui.pushButtonGotoMeasures.click()
    ui.pushButtonBackToMain1.click()
    assert ui.stackedWidget.currentIndex() == 0


def test_back_to_main_from_sessions(app):
    ui = app.ui
    ui.pushButtonGotoSessions.click()
    ui.pushButtonBackToMain2.click()
    assert ui.stackedWidget.currentIndex() == 0


def test_date_edit(app):
    ui = app.ui
    ui.pushButtonGotoDistribution.click()
    ui.dateEdit.setDate(QDate(2022, 1, 1))
    assert ui.dateEdit.date().toString('yyyy-MM-dd') == '2022-01-01'


def test_combobox_selection(app):
    ui = app.ui
    ui.pushButtonGotoDistribution.click()
    ui.comboBoxSessions.addItems(["EUR", "USD", "GBP", "JPY", "CHF"])
    ui.comboBoxDistribution1.setCurrentIndex(1)
    assert ui.comboBoxDistribution1.currentText() == "USD"
    ui.comboBoxDistribution1.setCurrentIndex(3)
    assert ui.comboBoxDistribution1.currentText() == "JPY"


if __name__ == "__main__":
    pytest.main()
