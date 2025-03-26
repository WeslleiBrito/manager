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

        itens: list[TDateComponent] = [{"legend": "Data inicial"}, {"legend": "Data final"}]
        self.component_dates = CustomDate(itens)

        # Layout principal
        layout = QVBoxLayout(self)

        # Adicionando filtros
        filter_layout = self.create_filter_date()
        layout.addItem(QSpacerItem(0, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
        layout.addLayout(filter_layout)

        # Adicionando o painel de resumo
        layout.addItem(self.sidebar_spacer)
        panel_resume = Panel(items)
        layout.addWidget(panel_resume)
        layout.addItem(self.sidebar_spacer)


    def create_filter_date(self):
        """Cria filtros para o dashboard"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_date = QHBoxLayout()
        #button_update.clicked.connect(self.update_values)

        period_label = QLabel("Período:")
        layout.addWidget(period_label)

        layout_date.addWidget(self.component_dates)
        layout_button_vert = QVBoxLayout()
        layout_button_vert.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        button_update = QPushButton("Atualizar")
        layout_button_vert.addWidget(button_update)
        layout_date.addLayout(layout_button_vert)

        layout.addLayout(layout_date)

        return layout




if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())