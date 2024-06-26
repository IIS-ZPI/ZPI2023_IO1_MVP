# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButtonGotoSessions = QPushButton(self.page)
        self.pushButtonGotoSessions.setObjectName(u"pushButtonGotoSessions")
        font = QFont()
        font.setPointSize(18)
        self.pushButtonGotoSessions.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButtonGotoSessions)

        self.pushButtonGotoMeasures = QPushButton(self.page)
        self.pushButtonGotoMeasures.setObjectName(u"pushButtonGotoMeasures")
        self.pushButtonGotoMeasures.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButtonGotoMeasures)

        self.pushButtonGotoDistribution = QPushButton(self.page)
        self.pushButtonGotoDistribution.setObjectName(u"pushButtonGotoDistribution")
        self.pushButtonGotoDistribution.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButtonGotoDistribution)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 0, 0, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonBackToMain3 = QPushButton(self.page_2)
        self.pushButtonBackToMain3.setObjectName(u"pushButtonBackToMain3")

        self.horizontalLayout_2.addWidget(self.pushButtonBackToMain3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout.addWidget(self.dateEdit)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBoxDistribution1 = QComboBox(self.groupBox_3)
        self.comboBoxDistribution1.setObjectName(u"comboBoxDistribution1")

        self.verticalLayout_3.addWidget(self.comboBoxDistribution1)

        self.comboBoxDistribution2 = QComboBox(self.groupBox_3)
        self.comboBoxDistribution2.setObjectName(u"comboBoxDistribution2")

        self.verticalLayout_3.addWidget(self.comboBoxDistribution2)


        self.gridLayout_3.addWidget(self.groupBox_3, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonMonth = QPushButton(self.groupBox_2)
        self.pushButtonMonth.setObjectName(u"pushButtonMonth")

        self.horizontalLayout_3.addWidget(self.pushButtonMonth)

        self.pushButtonQuarter = QPushButton(self.groupBox_2)
        self.pushButtonQuarter.setObjectName(u"pushButtonQuarter")

        self.horizontalLayout_3.addWidget(self.pushButtonQuarter)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.widgetDistribution = QWidget(self.page_2)
        self.widgetDistribution.setObjectName(u"widgetDistribution")
        self.widgetDistribution.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.widgetDistribution)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 0, 0, 1, 3)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_20, 8, 0, 1, 3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.pushButtonBackToMain2 = QPushButton(self.page_3)
        self.pushButtonBackToMain2.setObjectName(u"pushButtonBackToMain2")

        self.horizontalLayout_7.addWidget(self.pushButtonBackToMain2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)


        self.gridLayout.addLayout(self.horizontalLayout_7, 9, 0, 1, 3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.comboBoxSessions = QComboBox(self.page_3)
        self.comboBoxSessions.setObjectName(u"comboBoxSessions")

        self.horizontalLayout_6.addWidget(self.comboBoxSessions)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidgetSessions = QTableWidget(self.page_3)
        if (self.tableWidgetSessions.columnCount() < 3):
            self.tableWidgetSessions.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetSessions.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetSessions.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetSessions.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidgetSessions.rowCount() < 6):
            self.tableWidgetSessions.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetSessions.setVerticalHeaderItem(5, __qtablewidgetitem8)
        self.tableWidgetSessions.setObjectName(u"tableWidgetSessions")
        self.tableWidgetSessions.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidgetSessions.setAutoFillBackground(False)
        self.tableWidgetSessions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidgetSessions.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetSessions.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetSessions.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidgetSessions.setShowGrid(True)
        self.tableWidgetSessions.setSortingEnabled(False)
        self.tableWidgetSessions.setWordWrap(True)
        self.tableWidgetSessions.setCornerButtonEnabled(True)
        self.tableWidgetSessions.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetSessions.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidgetSessions.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetSessions.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.tableWidgetSessions)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 3, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 10, 0, 1, 3)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_12, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_2 = QGridLayout(self.page_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 6, 0, 1, 3)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.page_10)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.comboBoxMeasures = QComboBox(self.page_10)
        self.comboBoxMeasures.setObjectName(u"comboBoxMeasures")

        self.horizontalLayout_8.addWidget(self.comboBoxMeasures)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_20)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.tableWidgetMeasures = QTableWidget(self.page_10)
        if (self.tableWidgetMeasures.columnCount() < 4):
            self.tableWidgetMeasures.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetMeasures.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetMeasures.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetMeasures.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetMeasures.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        if (self.tableWidgetMeasures.rowCount() < 6):
            self.tableWidgetMeasures.setRowCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetMeasures.setVerticalHeaderItem(5, __qtablewidgetitem18)
        self.tableWidgetMeasures.setObjectName(u"tableWidgetMeasures")
        self.tableWidgetMeasures.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidgetMeasures.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetMeasures.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetMeasures.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidgetMeasures.setShowGrid(True)

        self.verticalLayout_13.addWidget(self.tableWidgetMeasures)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 3, 1, 1, 1)

        self.label_7 = QLabel(self.page_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 3, 2, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_19, 4, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)

        self.pushButtonBackToMain1 = QPushButton(self.page_10)
        self.pushButtonBackToMain1.setObjectName(u"pushButtonBackToMain1")

        self.horizontalLayout_9.addWidget(self.pushButtonBackToMain1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_22)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 5, 0, 1, 3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_10)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonGotoSessions.setText(QCoreApplication.translate("MainWindow", u"Sessions", None))
        self.pushButtonGotoMeasures.setText(QCoreApplication.translate("MainWindow", u"Statistical measures", None))
        self.pushButtonGotoDistribution.setText(QCoreApplication.translate("MainWindow", u"Change distribution", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Currency Analysis</span></p></body></html>", None))
        self.pushButtonBackToMain3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Change distribution</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"start date", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"currencies", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"period", None))
        self.pushButtonMonth.setText(QCoreApplication.translate("MainWindow", u"month", None))
        self.pushButtonQuarter.setText(QCoreApplication.translate("MainWindow", u"quarter", None))
        self.pushButtonBackToMain2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choosen currency:", None))
        ___qtablewidgetitem = self.tableWidgetSessions.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"rising sessions", None));
        ___qtablewidgetitem1 = self.tableWidgetSessions.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"falling sessions", None));
        ___qtablewidgetitem2 = self.tableWidgetSessions.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"unchanged sessions", None));
        ___qtablewidgetitem3 = self.tableWidgetSessions.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1 week", None));
        ___qtablewidgetitem4 = self.tableWidgetSessions.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2 weeks", None));
        ___qtablewidgetitem5 = self.tableWidgetSessions.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1 month", None));
        ___qtablewidgetitem6 = self.tableWidgetSessions.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1 quarter", None));
        ___qtablewidgetitem7 = self.tableWidgetSessions.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"half-year", None));
        ___qtablewidgetitem8 = self.tableWidgetSessions.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1 year", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Number of rising, unchanged and falling sessions</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Choosen currency:", None))
        ___qtablewidgetitem9 = self.tableWidgetMeasures.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"median", None));
        ___qtablewidgetitem10 = self.tableWidgetMeasures.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"dominant", None));
        ___qtablewidgetitem11 = self.tableWidgetMeasures.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"standard deviation", None));
        ___qtablewidgetitem12 = self.tableWidgetMeasures.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"coefficient of variation", None));
        ___qtablewidgetitem13 = self.tableWidgetMeasures.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1 week", None));
        ___qtablewidgetitem14 = self.tableWidgetMeasures.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"2 weeks", None));
        ___qtablewidgetitem15 = self.tableWidgetMeasures.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1 month", None));
        ___qtablewidgetitem16 = self.tableWidgetMeasures.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1 quarter", None));
        ___qtablewidgetitem17 = self.tableWidgetMeasures.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"half-year", None));
        ___qtablewidgetitem18 = self.tableWidgetMeasures.verticalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"1 year", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Statistical measures</span></p></body></html>", None))
        self.pushButtonBackToMain1.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

