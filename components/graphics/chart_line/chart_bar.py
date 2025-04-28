from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
import sys

list_product = [
    ["01/24", 232.15],
    ["02/24", 111.02],
    ["03/24", 189.47],
    ["04/24", 245.89],
    ["05/24", 132.34],
    ["06/24", 298.56],
    ["07/24", 210.77],
    ["08/24", 155.21],
    ["09/24", 267.90],
    ["10/24", 180.64],
    ["11/24", 223.45],
    ["12/24", 199.88],
    ["01/25", 276.12],
    ["02/25", 143.76],
    ["03/25", 187.55]
]

class ChartBar(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criar conjunto de barras
        bar_set = QBarSet("Vendas")

        # Adicionar valores
        for item in list_product:
            bar_set.append(item[1])

        # Criar série de barras
        series = QBarSeries()
        series.append(bar_set)

        # Criar o gráfico
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Vendas por Mês")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        # Eixo X - Datas como categorias
        axis_x = QBarCategoryAxis()
        categories = [item[0] for item in list_product]
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        # Eixo Y - Valores
        axis_y = QValueAxis()
        axis_y.setLabelFormat("%.2f")
        axis_y.setTitleText("Valor (R$)")
        axis_y.setRange(0, 400)
        axis_y.setTickCount(int(len(list_product) * 1.5))
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        # Visualização
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.setCentralWidget(chart_view)
        self.resize(900, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChartBar()
    window.show()
    sys.exit(app.exec())
