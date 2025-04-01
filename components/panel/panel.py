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
    """
        Classe que representa um painel de informações exibido em um formato gráfico.
        Cada painel contém múltiplos componentes que mostram um ícone, um valor e uma legenda,
        e possibilita a atualização desses valores dinamicamente.

        A classe herda de `QWidget` e é composta por um layout principal contendo
        vários widgets que representam os itens configurados na lista `list_itens`.

        A cada item na lista, um painel com o ícone associado, legenda e valor é criado.
        Esses valores podem ser atualizados posteriormente.

        Parâmetros:
        - list_itens (List[TItemPanel]): Lista de itens a serem exibidos no painel.
          Cada item deve ser um dicionário contendo as chaves 'pathIcon' (caminho do ícone SVG),
          'legend' (legenda a ser exibida), 'value' (valor a ser exibido), e opcionalmente 'unit' (unidade do valor).

        Exemplo de uso:
        - Para criar um painel com múltiplos itens:
            panel = Panel([
                {"pathIcon": "path_to_icon.svg", "legend": "Faturamento", "value": 183039.51},
                {"pathIcon": "path_to_icon.svg", "legend": "Lucro", "value": 9203.44}
            ])
            panel.show()
        """

    def __init__(self, list_itens: List[TItemPanel]):
        super().__init__()
        self.list_items = list_itens
        self.main_layout = QHBoxLayout()
        self.showMaximized()

        # Dicionário para armazenar os labels dos valores
        self.value_labels = {}

        for item in self.list_items:
            path_icon = Path(item["pathIcon"])

            if not path_icon.exists():
                print(f"O caminho do ícone informado não existe: {path_icon}")
                sys.exit(1)

            component_widget = QWidget()
            component_widget.setMaximumHeight(70)
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
            self._update_value_label(value_label, item["value"], item.get("unit"))

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

    @staticmethod
    def _update_value_label(label: QLabel, value: float, unit: str = None):
        """Atualiza o texto de um QLabel com o novo valor formatado."""
        value_formatted = format_value(value)
        if unit:
            label.setText(f"{unit} {value_formatted}")
        else:
            label.setText(f"R$ {value_formatted}")

    def _update_item(self, legend: str, new_value: float):
        """Atualiza um único item no painel e reflete a mudança na interface gráfica."""
        # Encontra o item na lista de itens
        for item in self.list_items:
            if item["legend"] == legend:
                item["value"] = new_value  # Atualiza a lista de itens
                unit = item.get("unit")  # Recupera a unidade, se existir
                # Atualiza o QLabel da interface gráfica, passando a unidade correta
                self._update_value_label(self.value_labels[legend], new_value, unit)
                break
        else:
            print(f"Legenda '{legend}' não encontrada no painel.")

    def update_value(self, updates: dict[str, float] | str, new_value: float):
        """
            Atualiza um ou múltiplos valores no painel com base na legenda ou no dicionário de atualizações.

            Parâmetros:
            - updates: Pode ser uma string representando uma legenda para atualização de um único valor ou um dicionário
                       onde as chaves são as legendas e os valores são os novos valores a serem atribuídos.
            - new_value: Valor a ser atribuído. Obrigatório se 'updates' for uma string.

            Exemplo de uso:
            - Atualizar um único valor:
                panel.update_value_or_values("Faturamento", 250000.00)
            - Atualizar múltiplos valores:
                panel.update_value_or_values({
                    "Faturamento": 250000.00,
                    "Lucro": 18000.00,
                    "Porcentagem": 15
                })
        """
        if isinstance(updates, dict):  # Atualiza múltiplos valores
            for legend, new_value in updates.items():
                self._update_item(legend, new_value)
        elif isinstance(updates, str):  # Atualiza um único valor
            self._update_item(updates, new_value)



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