from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem, QStackedWidget
)
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QByteArray
from interfaces.dashboard.dashboard import Dashboard

class Home(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        self.expanded = True
        self.width_expanded = 200
        self.width_collapsed = 60

        # Layout principal (sem margens, pois será aplicado apenas na sidebar)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 🔹 Layout intermediário para espaçamento da sidebar
        self.sidebar_container = QHBoxLayout()
        self.sidebar_container.setContentsMargins(10, 0, 10, 0)  # Margem externa apenas para a sidebar

        # 🔹 Espaçador antes da sidebar (margem esquerda)
        self.sidebar_spacer = QSpacerItem(20, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        # Criando a sidebar
        self.sidebar = QFrame()
        self.sidebar.setStyleSheet("background-color: #2c3e50; border-radius: 15px;")
        self.sidebar.setMinimumWidth(self.width_expanded)
        self.sidebar.setMaximumWidth(self.width_expanded)
        self.sidebar.setMaximumHeight(600)

        # Botão de alternância
        self.toggle_button = QPushButton("☰")
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.setStyleSheet("background-color: #34495e; color: white; border: none; font-size: 18px;")
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Botões da Sidebar para alternar telas
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_dashboard.clicked.connect(lambda: self.switch_page(0))

        self.btn_graficos = QPushButton("Gráficos")
        self.btn_graficos.clicked.connect(lambda: self.switch_page(1))

        self.btn_lista = QPushButton("Lista")
        self.btn_lista.clicked.connect(lambda: self.switch_page(2))

        # Layout da sidebar
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 40, 0, 0)
        self.sidebar_layout.addWidget(QLabel("Menu"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.btn_dashboard)
        self.sidebar_layout.addWidget(self.btn_graficos)
        self.sidebar_layout.addWidget(self.btn_lista)
        self.sidebar_layout.addStretch()

        # 🔹 Adiciona espaçador antes da sidebar dentro do container
        self.sidebar_container.addItem(self.sidebar_spacer)
        self.sidebar_container.addWidget(self.sidebar)

        # Criando as páginas no QStackedWidget
        self.pages = QStackedWidget()
        self.pages.addWidget(Dashboard())  # Página do Dashboard
        self.pages.addWidget(self.create_graficos_page())   # Página de Gráficos
        self.pages.addWidget(self.create_lista_page())      # Página de Lista

        # 🔹 Adiciona container da sidebar e conteúdo ao layout principal
        self.main_layout.addLayout(self.sidebar_container)
        self.main_layout.addWidget(self.pages)

        # Configuração inicial para exibir a primeira página (Dashboard)
        self.pages.setCurrentIndex(0)

        # Animação para expandir/recolher
        self.animation = QPropertyAnimation(self.sidebar, QByteArray(b"minimumWidth"))
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    def create_dashboard_page(self):
        """Cria a página do Dashboard."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📊 Dashboard - Aqui ficam os KPIs"))
        return page

    def create_graficos_page(self):
        """Cria a página de Gráficos."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📈 Gráficos - Visualizações dos dados"))
        return page

    def create_lista_page(self):
        """Cria a página de Lista."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📋 Lista - Informações detalhadas"))
        return page

    def switch_page(self, index):
        """Alterna entre as páginas no QStackedWidget."""
        self.pages.setCurrentIndex(index)

    def toggle_sidebar(self):
        """Expande ou recolhe a sidebar com animação."""
        if self.expanded:
            self.animation.setStartValue(self.width_expanded)
            self.animation.setEndValue(self.width_collapsed)
            self.sidebar.setMaximumWidth(self.width_collapsed)
        else:
            self.animation.setStartValue(self.width_collapsed)
            self.animation.setEndValue(self.width_expanded)
            self.sidebar.setMaximumWidth(self.width_expanded)

        self.animation.start()
        self.expanded = not self.expanded


if __name__ == "__main__":
    app = QApplication([])
    window = Home()
    window.show()
    app.exec()
