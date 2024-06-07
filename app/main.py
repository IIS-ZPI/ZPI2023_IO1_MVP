# You can ran this file from the root directory of the project by running `python -m app.main`
from datetime import date, datetime, timedelta

from PySide6.QtCore import QDate, QObject
from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QMainWindow, QButtonGroup, QHeaderView, \
    QAbstractItemView
from .app_ui import Ui_MainWindow
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from .constans import AnalysisPeriod
from .api import get_sessions_data, get_statistical_measures, get_changes_distribution


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(800, 600)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.setup_main_page()

        self.setup_distribution_page()

        self.setup_sessions_page()

        self.setup_measures_page()

    def setup_main_page(self):
        self.ui.pushButtonGotoDistribution.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonGotoSessions.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButtonGotoMeasures.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

    def setup_sessions_page(self):
        self.ui.pushButtonBackToMain2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.comboBoxSessions.addItems(["EUR", "USD", "GBP", "JPY", "CHF"])
        self.ui.tableWidgetSessions.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidgetSessions.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableWidgetSessions.horizontalHeader().setSectionsClickable(False)
        self.ui.tableWidgetSessions.verticalHeader().setSectionsClickable(False)
        self.ui.comboBoxSessions.setCurrentIndex(0)
        self.ui.comboBoxSessions.currentIndexChanged.connect(self.on_update_sessions)

        self.on_update_sessions()

    def on_update_sessions(self):
        for period in AnalysisPeriod:
            data = get_sessions_data(self.ui.comboBoxSessions.currentText(), period)
            i = 0
            for value in data:
                item = QTableWidgetItem(str(value))
                self.ui.tableWidgetSessions.setItem(period.value - 1, i, item)
                i += 1

    def setup_measures_page(self):
        self.ui.pushButtonBackToMain1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.comboBoxMeasures.addItems(["EUR", "USD", "GBP", "JPY", "CHF"])
        self.ui.comboBoxMeasures.setCurrentIndex(0)
        self.ui.tableWidgetMeasures.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidgetMeasures.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableWidgetMeasures.horizontalHeader().setSectionsClickable(False)
        self.ui.tableWidgetMeasures.verticalHeader().setSectionsClickable(False)
        self.on_update_measures()
        self.ui.comboBoxMeasures.currentIndexChanged.connect(self.on_update_measures)

    def on_update_measures(self):
        for period in AnalysisPeriod:
            data = get_statistical_measures(self.ui.comboBoxMeasures.currentText(), period)
            i = 0
            for value in data:
                item = QTableWidgetItem(str(value.__format__("0.6f")))
                self.ui.tableWidgetMeasures.setItem(period.value - 1, i, item)
                i += 1

    def setup_distribution_page(self):
        self.ui.pushButtonBackToMain3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        today = date.today() - timedelta(days=29)
        self.ui.dateEdit.setDate(QDate(today.year, today.month, today.day))
        self.ui.comboBoxDistribution1.addItems(["EUR", "USD", "GBP", "JPY", "CHF"])
        self.ui.comboBoxDistribution2.addItems(["EUR", "USD", "GBP", "JPY", "CHF"])
        self.ui.comboBoxDistribution2.setCurrentIndex(1)
        self.ui.comboBoxDistribution1.setCurrentIndex(0)

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.ui.pushButtonMonth)
        self.buttonGroup.addButton(self.ui.pushButtonQuarter)
        self.buttonGroup.setExclusive(True)

        self.ui.pushButtonMonth.setCheckable(True)
        self.ui.pushButtonMonth.setChecked(True)
        self.ui.pushButtonQuarter.setCheckable(True)
        self.ui.pushButtonQuarter.setChecked(False)

        hist, bins = get_changes_distribution(
            self.ui.comboBoxDistribution1.currentText(),
            self.ui.comboBoxDistribution2.currentText(),
            self.ui.dateEdit.date().toPython(),
            AnalysisPeriod.MONTH)

        self.canvas = MplCanvas(hist, bins)

        self.ui.verticalLayout_4.replaceWidget(self.ui.widgetDistribution, self.canvas)
        self.ui.widgetDistribution.deleteLater()

        self.buttonGroup.buttonClicked.connect(self.on_update_distribution)
        self.ui.comboBoxDistribution1.currentIndexChanged.connect(self.on_update_distribution)
        self.ui.comboBoxDistribution2.currentIndexChanged.connect(self.on_update_distribution)
        self.ui.dateEdit.dateChanged.connect(self.on_update_distribution)

    def on_update_distribution(self):
        hist, bins = get_changes_distribution(
            self.ui.comboBoxDistribution1.currentText(),
            self.ui.comboBoxDistribution2.currentText(),
            self.ui.dateEdit.date().toPython(),
            AnalysisPeriod.MONTH if self.ui.pushButtonMonth.isChecked() else AnalysisPeriod.QUARTER)

        self.canvas.plot_data(hist, bins)


class MplCanvas(FigureCanvas):
    def __init__(self, hist, bins):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.plot_data(hist, bins)

    def plot_data(self, hist, bins):
        self.ax.clear()
        self.ax.hist(bins[:-1], bins, weights=hist, edgecolor='black')
        self.draw()


if __name__ == "__main__":
    try:
        app = QApplication()
        window = MainWindow()
        window.setWindowTitle("Currency Analysis")
        window.show()
        app.exec()
    except Exception as e:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("Error")
        msg_box.setDetailedText(str(e))
        msg_box.setWindowTitle("Error")
        msg_box.exec()
