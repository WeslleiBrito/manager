from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from pathlib import Path
import sys

from components.panel.customDate import CustomDate
from components.panel.panel import Panel
from components.graphics.item_billing.invoicing import TableView
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

        data = [
            [1, 101, "Teclado Mecânico", 3, 3911.17, 1635.02, 163.50, 81.75, 114.45, -236.64, -10.61, "Carlos"],
            [2, 109, "Webcam Full HD", 8, 2649.01, 1495.25, 149.53, 74.76, 104.67, 142.54, 7.25, "Carlos"],
            [3, 102, "Mouse Gamer", 10, 368.32, 279.18, 27.92, 13.96, 19.54, 63.28, 15.67, "Ana"],
            [4, 103, "Monitor 24''", 4, 2319.14,1913.52, 191.35, 95.68, 133.95, 276.29, 10.58, "Fernanda"],
            [5, 106, "SSD 1TB", 7, 901.05, 430.34, 43.03, 21.52, 30.12, 41.01, 7.25, "Carlos"],
            [6, 110, "Impressora Laser", 2, 1113.41, 825.99, 82.60, 41.30, 57.82, 96.48, 11.69, "Lucas"],
            [7, 107, "Placa de Vídeo", 5, 4033.55, 2899.99, 290.00, 145.00, 203.00, 362.00, 9.75, "João"],
            [8, 112, "Notebook i5", 3, 7912.13, 4500.00, 450.00, 225.00, 315.00, 510.00, 11.33, "Fernanda"],
            [9, 115, "Cadeira Gamer", 6, 2421.07, 1350.75, 135.08, 67.54, 94.55, 176.00, 9.87, "Ana"],
            [10, 118, "Fone Bluetooth", 9, 393.00, 279.90, 27.99, 13.99, 19.59, 36.32, 11.48, "Carlos"],
        ]

        headers = [
            "Nº Venda", "Cód. Produto", "Descrição", "Quantidade", "Faturamento", "Custo",
            "Despesa Fixa", "Despesa Variável", "Comissão", "Lucro R$", "Lucro %", "Vendedor"
        ]
        self.button_update = QPushButton("Atualizar tabela")
        self.button_update.clicked.connect(self.update_data_table)

        self.novos_dados = [
            [11, 120, "Monitor 27''", 2, 2899.00, 1999.99, 200.00, 100.00, 140.00, -260.00, -9.99, "Bruno"],
            [12, 121, "Teclado RGB", 5, 599.00, 299.99, 30.00, 15.00, 21.00, 50.00, 8.35, "Fernanda"]
        ]


        items_date: list[TDateComponent] = [{"legend": "Data inicial"}, {"legend": "Data final"}]
        self.component_dates = CustomDate(items_date)
        # Layout principal
        layout = QVBoxLayout(self)
        # Adicionando filtros
        filter_layout = self.create_filter_date()
        layout.addLayout(filter_layout)

        # Adicionando o painel de resumo
        self.table_itens = TableView(data, headers)
        self.table_itens.itemDoubleClicked.connect(self.print_item)

        self.panel_resume = Panel(items)
        layout_panel = QVBoxLayout(self.panel_resume)
        layout.addLayout(layout_panel)
        layout.addWidget(self.panel_resume)
        layout.addWidget(self.table_itens)
        layout.addWidget(self.button_update)

        # Adicionando a tabela de vendas por item



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


    def print_item(self, data_item: list):
        print(data_item)

    def update_data_table(self):
        self.table_itens.update_data(self.novos_dados)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())