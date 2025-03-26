# -*- coding: utf-8 -*-
import sys
from PySide6.QtCore import QMetaObject, QDate
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QDateEdit, QPushButton, QSizePolicy, QSpacerItem
from typing import List
from my_types.my_types import TDateComponent
from datetime import date

class CustomDate(QWidget):
    def __init__(self, items: List[TDateComponent], with_button: bool = False):
        super().__init__()

        self.items = items
        self.list_component_date = []
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.with_button = with_button
        self.list_dates: list[QDateEdit] = []

        self.setup_ui()


    def setup_ui(self):

        for item in self.items:

            name = item["legend"]

            default_date = item.get("default_date", QDate.currentDate())
            with_calendar = item.get("with_calendar", True)
            display_format = item.get("display_format", "dd/MM/yyyy")

            widget = QWidget(self)
            widget.setFixedHeight(80)

            vertical_layout = QVBoxLayout(widget)
            legend = QLabel(name, widget)

            date_edit = QDateEdit(widget)


            if "min_date" in item:
                date_edit.setMinimumDate(item["min_date"])

            if "max_date" in item:
                date_edit.setMaximumDate(item["max_date"])

            date_edit.setDisplayFormat(display_format)
            date_edit.setCalendarPopup(with_calendar)
            date_edit.setDate(default_date)

            vertical_layout.addWidget(legend)
            vertical_layout.addWidget(date_edit)

            self.horizontalLayout.addWidget(widget)

            self.list_dates.append(date_edit)


        # Botão Atualizar
        if self.with_button:
            widget_button = QWidget(self)
            widget_button.setFixedHeight(80)

            vertical_layout_button = QVBoxLayout(widget_button)
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            button_update = QPushButton("Atualizar", widget_button)
            button_update.clicked.connect(self.get_dates)

            vertical_layout_button.addItem(vertical_spacer)
            vertical_layout_button.addWidget(button_update)

            self.horizontalLayout.addWidget(widget_button)

        QMetaObject.connectSlotsByName(self)  # Conectar sinais e slots automaticamente


    def get_dates(self) -> list[date]:
        dates = [date(item_date.date().year(), item_date.date().month(), item_date.date().day()) for item_date in self.list_dates]
        return dates


    def get_date_item(self, index: int) -> date:
        if index < 0 or index >= len(self.list_dates):
            raise IndexError("Índice fora do intervalo válido")

        date_selected = self.list_dates[index].date()
        return date(date_selected.year(), date_selected.month(), date_selected.day())



if __name__ == "__main__":
    itens: List[TDateComponent] = [{"legend": "Data inicial"}, {"legend": "Data final"}]
    app = QApplication(sys.argv)
    window = CustomDate(itens)
    window.show()
    sys.exit(app.exec())
