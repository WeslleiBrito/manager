from typing import TypedDict, NotRequired
from PySide6.QtCore import QDate
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtGui import QFont, QColor

class TDateComponent(TypedDict):
    legend: str
    default_date: NotRequired[QDate]
    with_calendar: NotRequired[bool]
    display_format: NotRequired[str]
    min_date: NotRequired[QDate | None]
    max_date: NotRequired[QDate | None]


class TableStyle(TypedDict, total=False):
    font: QFont  # Fonte padrão da tabela
    headerFont: QFont  # Fonte do cabeçalho
    textColor: QColor  # Cor do texto padrão
    backgroundColor: QColor  # Cor de fundo da tabela
    headerTextColor: QColor  # Cor do texto do cabeçalho
    headerBackgroundColor: QColor  # Cor de fundo do cabeçalho
    alternatingRowColors: bool  # Alternância de cores nas linhas
    showGrid: bool  # Exibir grade
    gridStyle: Qt.PenStyle  # Estilo da grade
    selectionBehavior: QAbstractItemView.SelectionBehavior  # Comportamento de seleção (linha, célula)
    selectionMode: QAbstractItemView.SelectionMode  # Modo de seleção (única, múltipla)
    rowHeight: int  # Altura da linha
    columnWidth: int  # Largura das colunas
    highlightColor: QColor  # Cor de destaque ao selecionar uma célula
    borderColor: QColor  # Cor da borda da tabela

class CellStyle(TypedDict, total=False):
    textColor: QColor  # Cor do texto padrão da célula
    negativeTextColor: QColor  # Cor do texto para valores negativos
    positiveTextColor: QColor  # Cor do texto para valores positivos
    backgroundColor: QColor  # Cor de fundo da célula
    borderColor: QColor  # Cor da borda da célula
    alignment: Qt.AlignmentFlag  # Alinhamento do texto na célula
    padding: int  # Espaçamento interno na célula
    font: QFont  # Fonte específica para as células

class TTableTheme(TypedDict, total=False):
    table: TableStyle
    cell: CellStyle