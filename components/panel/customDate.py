from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QDateEdit, QLabel, QVBoxLayout
from datetime import date

class CustomDate(QWidget):
    def __init__(self, legend: str, default_date: QDate = QDate.currentDate(),
                 with_calendar: bool = True, display_format: str = "dd/MM/yyyy",
                 min_date: QDate = None, max_date: QDate = None, maximum_width: int = 90):
        super().__init__()

        self.date = QDateEdit(self)

        self.setContentsMargins(0, 0, 0, 0)

        if min_date:
            self.date.setMinimumDate(min_date)

        if max_date:
            self.date.setMaximumDate(max_date)

        self.legend = QLabel(legend)

        self.date.setDate(default_date)
        self.date.setDisplayFormat(display_format)
        self.date.setCalendarPopup(with_calendar)
        self.date.setMaximumWidth(maximum_width)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.legend)
        self.layout.addWidget(self.date)

        self.layout.setSpacing(0)

        self.setLayout(self.layout)

    def get_date(self):
        """Obtém e exibe a data selecionada"""
        selected_date = self.date.date()
        return date(selected_date.year(), selected_date.month(), selected_date.day())