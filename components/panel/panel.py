from typing import List, TypedDict, NotRequired
import sys
from PySide6.QtCore import QSize, Qt, QByteArray
import locale
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication
from pathlib import Path
from PySide6.QtSvgWidgets import QSvgWidget


path_local = Path(__file__).parent
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_value(value: float) -> str:
    return locale.format_string('%.2f', value, grouping=True, monetary=True)


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
    unit: NotRequired[str]


class Panel(QWidget):
    def __init__(self, list_itens: List[TItemPanel]):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.showMaximized()

        # Dicionário para armazenar os labels dos valores
        self.value_labels = {}

        for item in list_itens:
            path_icon = Path(item["pathIcon"])

            if not path_icon.exists():
                print(f"O caminho do ícone informado não existe: {path_icon}")
                sys.exit(1)

            component_widget = QWidget()
            component_widget.setStyleSheet("""
                background-color: #D9D9D9;
                color: #000000;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            """)

            component_layout = QHBoxLayout(component_widget)
            layout_value = QVBoxLayout()

            icon = QSvgWidget(item["pathIcon"])
            icon.setFixedSize(QSize(40, 40))

            legend = QLabel(item['legend'])
            legend.setStyleSheet("""
                font-weight: bold;
                font-size: 12px
            """)

            value_label = QLabel()
            self.update_value_label(value_label, item["value"], item.get("unit"))

            value_label.setStyleSheet("""
                font-weight: 600;
                font-size: 16px
            """)

            # Armazena o label no dicionário
            self.value_labels[item["legend"]] = value_label

            layout_value.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout_value.addWidget(legend, alignment=Qt.AlignmentFlag.AlignCenter)

            component_layout.addWidget(icon)
            component_layout.addLayout(layout_value)

            self.main_layout.addWidget(component_widget)

        self.setLayout(self.main_layout)

    def update_value_label(self, label: QLabel, value: float, unit: str = None):
        """Atualiza o texto de um QLabel com o novo valor formatado."""
        value_formatted = format_value(value)
        if unit:
            label.setText(f"{unit} {value_formatted}")
        else:
            label.setText(f"R$ {value_formatted}")

    def update_value(self, legend: str, new_value: float):
        """Atualiza o valor de um item no painel."""
        if legend in self.value_labels:
            self.update_value_label(self.value_labels[legend], new_value)
        else:
            print(f"Legenda '{legend}' não encontrada no painel.")




if __name__ == "__main__":

    items: List[TItemPanel] = [
        {"pathIcon": str(path_local / "../../src/icons/dashboard/invoicing.svg"), "legend": "Faturamento",
         "value": 183039.51},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/cost.svg"), "legend": "Custo", "value": 92231.77},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/fixed-expenses.svg"), "legend": "Despesas Fixas",
         "value": 28325.11},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/variable-expenses.svg"),
         "legend": "Despesas Variáveis", "value": 14136.01},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/profit.svg"), "legend": "Lucro", "value": 9203.44},
        {"pathIcon": str(path_local / "../../src/icons/dashboard/percent.svg"), "legend": "Porcentagem", "value": 10, "unit": "%"},
    ]

    app = QApplication(sys.argv)
    panel = Panel(items)
    panel.show()
    sys.exit(app.exec())