
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, \
    QTableWidget, QTableWidgetItem, QSpacerItem, QSizePolicy
from PySide6.QtCharts import QChartView, QLineSeries, QChart
from PySide6.QtGui import QPainter
import random
from pathlib import Path
import sys
from components.panel.panel import Panel


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
            {"pathIcon": str(path_local / "../../src/icons/dashboard/percent.svg"), "legend": "Porcentagem",
             "value": 10},
        ]

        # Layout principal
        layout = QVBoxLayout(self)

        # Adicionando filtros
        filter_layout = self.create_filters()
        layout.addLayout(filter_layout)

        # Adicionando o gráfico
        #sales_chart = self.create_sales_chart()
        #layout.addWidget(sales_chart)

        # Adicionando o painel de resumo
        layout.addItem(self.sidebar_spacer)
        panel_resume = Panel(items)
        layout.addWidget(panel_resume)
        layout.addItem(self.sidebar_spacer)

        # Adicionando o resumo
        summary_layout = self.create_summary()
        layout.addLayout(summary_layout)

        # Adicionando a tabela de vendas
        sales_table = self.create_sales_table()
        layout.addWidget(sales_table)

    def create_filters(self):
        """Cria filtros para o dashboard"""
        layout = QHBoxLayout()

        period_label = QLabel("Período:")
        period_combo = QComboBox()
        period_combo.addItems(["Mês", "Trimestre", "Ano"])

        filter_button = QPushButton("Aplicar Filtro")
        filter_button.clicked.connect(self.apply_filter)

        layout.addWidget(period_label)
        layout.addWidget(period_combo)
        layout.addWidget(filter_button)

        return layout

    def create_sales_chart(self):
        """Cria o gráfico de vendas"""
        series = QLineSeries()
        for i in range(10):
            series.append(i, random.randint(50, 100))

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Vendas ao Longo do Tempo")

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        return chart_view

    def create_summary(self):
        """Cria um resumo das vendas"""
        layout = QHBoxLayout()
        total_sales_label = QLabel("Vendas Totais: R$ 50,000")
        total_sales_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(total_sales_label)
        layout.addStretch()
        return layout

    def create_sales_table(self):
        """Cria a tabela de vendas"""
        table = QTableWidget()
        table.setRowCount(5)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Total"])

        # Preenchendo a tabela com dados fictícios
        for row in range(5):
            table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            table.setItem(row, 1, QTableWidgetItem(f"Produto {row + 1}"))
            table.setItem(row, 2, QTableWidgetItem(str(random.randint(1, 10))))
            table.setItem(row, 3, QTableWidgetItem(f"R$ {random.randint(100, 500)}"))

        return table

    def apply_filter(self):
        """Aplica o filtro selecionado"""
        print("Filtro aplicado (exemplo: período de vendas)")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())