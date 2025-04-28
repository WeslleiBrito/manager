from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView, QAbstractItemView
from PySide6.QtCore import QAbstractTableModel, Qt, QSortFilterProxyModel, QModelIndex, Signal
from PySide6.QtGui import QBrush, QColor, QFont
from my_types.my_types import TTableTheme

DEFAULT_THEME: TTableTheme = {
    "table": {
        "font": QFont("Arial", 10),
        "headerFont": QFont("Arial", 10, QFont.Weight.Bold),
        "textColor": QColor("black"),
        "backgroundColor": QColor("white"),
        "headerTextColor": QColor("white"),
        "headerBackgroundColor": QColor("gray"),
        "alternatingRowColors": True,
        "showGrid": True,
        "gridStyle": Qt.PenStyle.SolidLine,
        "selectionBehavior": QAbstractItemView.SelectionBehavior.SelectRows,
        "selectionMode": QAbstractItemView.SelectionMode.SingleSelection,
        "rowHeight": 25,
        "columnWidth": 100,
        "highlightColor": QColor("blue"),
        "borderColor": QColor("black")
    },
    "cell": {
        "textColor": QColor("black"),
        "negativeTextColor": QColor("red"),
        "positiveTextColor": QColor("black"),
        "backgroundColor": QColor("white"),
        "borderColor": QColor("gray"),
        "alignment": Qt.AlignmentFlag.AlignRight,
        "padding": 5,
        "font": QFont("Arial", 10)
    }
}

class TableModel(QAbstractTableModel):
    def __init__(self, data, headers, theme=None, parent=None):
        super().__init__(parent)
        self._data = data
        self._headers = headers
        self.theme = {**DEFAULT_THEME, **(theme or {})}  # Aplica o tema padrão e sobrescreve com os valores fornecidos

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        value = self._data[index.row()][index.column()]
        cell_theme = self.theme["cell"]

        if role == Qt.ItemDataRole.DisplayRole:
            return value

        if role == Qt.ItemDataRole.ForegroundRole:
            if isinstance(value, (int, float)) and value < 0:
                return QBrush(cell_theme.get("negativeTextColor", QColor("red")))
            return QBrush(cell_theme.get("textColor", QColor("black")))

        if role == Qt.ItemDataRole.BackgroundRole:
            return QBrush(cell_theme.get("backgroundColor", QColor("white")))

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return cell_theme.get("alignment", Qt.AlignmentFlag.AlignLeft)

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
        return None

class TableView(QWidget):
    itemDoubleClicked = Signal(list)

    def __init__(self, data, headers, theme=None, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.data = data
        self.model = TableModel(self.data, headers, theme)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setSortCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        self.table = QTableView()
        self.table.setModel(self.proxy_model)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.apply_theme({**DEFAULT_THEME, **(theme or {})})

        self.table.doubleClicked.connect(self.on_item_double_clicked)

        layout.addWidget(self.table)
        self.setLayout(layout)

    def on_item_double_clicked(self, index: QModelIndex):
        row = index.row()
        row_data = [self.proxy_model.data(self.proxy_model.index(row, col)) for col in range(self.model.columnCount())]
        self.itemDoubleClicked.emit(row_data)

    def update_data(self, new_data: list):
        self.model.beginResetModel()
        self.model._data = new_data
        self.model.endResetModel()

    def apply_theme(self, theme):
        """ Aplica a estilização da tabela """

        if "font" in theme:
            self.table.setFont(theme["font"])

        if "headerFont" in theme:
            self.table.horizontalHeader().setFont(theme["headerFont"])

        if "textColor" in theme:
            self.table.setStyleSheet(f"color: {theme['textColor'].name()};")

        if "backgroundColor" in theme:
            self.table.setStyleSheet(f"background-color: {theme['backgroundColor'].name()};")

        if "headerTextColor" in theme and "headerBackgroundColor" in theme:
            self.table.setStyleSheet(f"""
                QHeaderView::section {{
                    color: {theme['headerTextColor'].name()};
                    background-color: {theme['headerBackgroundColor'].name()};
                }}
            """)

        if "alternatingRowColors" in theme:
            self.table.setAlternatingRowColors(theme["alternatingRowColors"])

        if "showGrid" in theme:
            self.table.setShowGrid(theme["showGrid"])

        if "gridStyle" in theme:
            if isinstance(theme["gridStyle"], int):  # Converte para Qt.PenStyle se necessário
                theme["gridStyle"] = Qt.PenStyle(theme["gridStyle"])
            self.table.setGridStyle(theme["gridStyle"])

        if "selectionBehavior" in theme:
            self.table.setSelectionBehavior(theme["selectionBehavior"])

        if "selectionMode" in theme:
            self.table.setSelectionMode(theme["selectionMode"])

        if "rowHeight" in theme:
            self.table.verticalHeader().setDefaultSectionSize(theme["rowHeight"])

        if "columnWidth" in theme:
            for i in range(self.table.model().columnCount()):
                self.table.setColumnWidth(i, theme["columnWidth"])
