from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from pathlib import Path
import sys

from components.panel.customDate import CustomDate
from components.panel.panel import Panel
from my_types.my_types import TDateComponent

path_local = Path(__file__).parent


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_spacer = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.button_update_panel = QPushButton("Atualizar painel")
        self.button_update_panel.clicked.connect(self.update_panel)

        items = [
            {"pathIcon": str(path_local / "../../src/icons/dashboard/invoicing.svg"), "legend": "Faturamento",
             "value": 183039.51},
            {"pathIcon": str(path_local / "../../src/icons/dashboard/cost.svg"), "legend": "Custo", "value": 92231.77},
            {"pathIcon": str(path_local / "../../src/icons/dashboard/fixed-expenses.svg"), "legend": "Despesas Fixas", "value": 28325.11},
            {"pathIcon": str(path_local / "../../src/icons/dashboard/variable-expenses.svg"), "legend": "Despesas Variáveis", "value": 14136.01},
            {"pathIcon": str(path_local / "../../src/icons/dashboard/profit.svg"), "legend": "Lucro", "value": 9203.44},
            {"pathIcon": str(path_local / "../../src/icons/dashboard/percent.svg"), "legend": "Porcentagem", "unit": "%",
             "value": 10},
        ]

        items_date: list[TDateComponent] = [{"legend": "Data inicial"}, {"legend": "Data final"}]
        self.component_dates = CustomDate(items_date)
        # Layout principal
        layout = QVBoxLayout(self)
        # Adicionando filtros
        filter_layout = self.create_filter_date()
        layout.addLayout(filter_layout)

        # Adicionando o painel de resumo

        self.panel_resume = Panel(items)
        layout_panel = QVBoxLayout(self.panel_resume)
        layout.addLayout(layout_panel)
        layout.addWidget(self.panel_resume)
        layout.addWidget(self.button_update_panel)

    def update_panel(self):
        self.panel_resume.update_value("Faturamento", 50000)

    def create_filter_date(self):
        """Cria filtros para o dashboard"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_date = QHBoxLayout()

        period_label = QLabel("Período:")
        period_label.setMaximumHeight(20)
        layout.addWidget(period_label)

        widget_button = QWidget()
        widget_button.setMaximumHeight(80)

        vertical_layout_button = QVBoxLayout(widget_button)
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        button_update = QPushButton("Atualizar")

        vertical_layout_button.addItem(vertical_spacer)
        vertical_layout_button.addWidget(button_update)

        layout_date.addWidget(self.component_dates)
        layout_date.addWidget(widget_button)


        layout.addLayout(layout_date)

        return layout




if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())