from typing import List, TypedDict
import sys
from PySide6.QtCore import QSize, Qt, QMargins, QByteArray

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication
from pathlib import Path
from PySide6.QtSvgWidgets import QSvgWidget


path_local = Path(__file__).parent


def load_svg_with_color(path: str, color: str) -> QByteArray:
    with open(path, "r", encoding="utf-8") as file:
        svg_content = file.read()

    # Substituir a cor atual do 'fill' pela nova cor
    new_svg_content = svg_content.replace('fill=', f'fill="{color}"')

    # Converter para QByteArray para carregar no QSvgWidget
    return QByteArray(new_svg_content.encode())


class TItemPanel(TypedDict):
    pathIcon: str
    legend: str
    value: float


class Panel(QWidget):
    def __init__(self, list_itens: List[TItemPanel]):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.showMaximized()

        for item in list_itens:
            path_icon = Path(item["pathIcon"])

            if not path_icon.exists():
                print(f"O caminho do ícone informado não existe: {path_icon}")
                sys.exit(1)

            # Criar um QWidget para segurar o layout e aplicar estilos nele
            component_widget = QWidget()
            component_widget.setStyleSheet("""
                background-color: #696969;
                color: #000000;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            """)

            component_layout = QHBoxLayout(component_widget)
            layout_value = QVBoxLayout()


            icon = QSvgWidget(item["pathIcon"])
            icon.setFixedSize(QSize(40, 40))
            #svg_icon = load_svg_with_color(item["pathIcon"], "#FFFFFF")

            #icon.load(svg_icon)
            legend = QLabel(item["legend"])

            value = QLabel(str(item["value"]))
            value.setStyleSheet("""
                font-weight: 600;
            """)

            layout_value.addWidget(legend, alignment=Qt.AlignmentFlag.AlignCenter)
            layout_value.addWidget(value, alignment=Qt.AlignmentFlag.AlignCenter)

            component_layout.addWidget(icon)
            component_layout.addLayout(layout_value)

            self.main_layout.addWidget(component_widget)  # Adiciona o widget estilizado ao layout principal

        self.setLayout(self.main_layout)



if __name__ == "__main__":

    items = [
        {"pathIcon": str(path_local / "../../src/icons/dashboard/invoicing.svg"), "legend": "Faturamento",
         "value": 183039.51},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/cost.svg"), "legend": "Custo", "value": 92231.77},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/fixed-expenses.svg"), "legend": "Despesas Fixas",
         "value": 28325.11},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/variable-expenses.svg"),
         "legend": "Despesas Variáveis", "value": 14136.01},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/profit.svg"), "legend": "Lucro", "value": 9203.44},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/percent.svg"), "legend": "Porcentagem", "value": 10},
    ]

    app = QApplication(sys.argv)
    panel = Panel(items)
    panel.show()
    sys.exit(app.exec())