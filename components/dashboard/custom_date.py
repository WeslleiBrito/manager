# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'designerpVGqEL.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


class CustomDate(object):
    def setup_ui(self, form):
        if not form.objectName():
            form.setObjectName(u"Form")
        form.resize(400, 300)

        self.widget = QWidget(form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 29, 323, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_date_initial = QWidget(self.widget)
        self.widget_date_initial.setObjectName(u"widget_date_initial")
        self.widget_date_initial.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_date_initial.setAutoFillBackground(False)
        self.widget_date_initial.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_date_initial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_date_initial)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.dateEdit = QDateEdit(self.widget_date_initial)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)


        self.horizontalLayout.addWidget(self.widget_date_initial)

        self.frame_date_final = QWidget(self.widget)
        self.frame_date_final.setObjectName(u"frame_date_final")
        self.verticalLayout_2 = QVBoxLayout(self.frame_date_final)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_date_final)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.frame_date_final)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEdit_2)


        self.horizontalLayout.addWidget(self.frame_date_final)

        self.frame_date_final_2 = QWidget(self.widget)
        self.frame_date_final_2.setObjectName(u"frame_date_final_2")
        self.verticalLayout_3 = QVBoxLayout(self.frame_date_final_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame_date_final_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_date_final_2)


        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data inicial", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Data final", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Atualizar", None))
    # retranslateUi



if __name__ == "__main__":
    app = QApplication(sys.argv)
    custom_date = CustomDate()
    custom_date.show()
    sys.exit(app.exec())