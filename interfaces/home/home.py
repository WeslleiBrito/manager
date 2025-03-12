from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem, QStackedWidget
)
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QByteArray, QSize
from interfaces.dashboard.dashboard import Dashboard
from pathlib import Path
import sys


class Home(QWidget):
    def __init__(self):
        super().__init__()
        path_local = Path(__file__).parent

        relative_paths_icons = [
            "../../src/icons/home-white.png",
            "../../src/icons/home-black.svg",
            "../../src/icons/menu.png",
            "../../src/icons/menu-2.png",
        ]

        self.path_icons = {}


        for path in relative_paths_icons:
            if not (path_local / path).exists():
                print(f"Erro: A imagem {path_local / path} não foi encontrada.")
                sys.exit(1)

            file_name = path[path.rfind("/") + 1: path.rfind(".")]

            key_name = []
            for index, character in enumerate(file_name):
                char_item = character

                if not character.isalnum():
                    char_item = "_"

                key_name.append(char_item)

            self.path_icons["".join(key_name)] = path_local / path

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
        self.sidebar.setStyleSheet("background-color: #03588C; border-radius: 15px;")
        self.sidebar.setMinimumWidth(self.width_expanded)
        self.sidebar.setMaximumWidth(self.width_expanded)
        self.sidebar.setMaximumHeight(600)

        # Botão de alternância
        self.toggle_button = QPushButton()
        self.toggle_button.setIcon(QIcon(str(self.path_icons["menu_2"])))
        self.toggle_button.setIconSize(QSize(30, 30))
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.setStyleSheet("background-color: #41AEF2; color: #FFFFFF; font-size: 18px; border-radius: 10px;")
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Botões da Sidebar para alternar telas
        self.btn_dashboard = QPushButton()
        self.btn_dashboard.setIcon(QIcon(str(self.path_icons["home_white"])))
        self.btn_dashboard.setIconSize(QSize(30, 30))
        self.btn_dashboard.setFixedSize(40, 40)
        self.btn_dashboard.clicked.connect(lambda: self.switch_page(0))

        self.btn_graficos = QPushButton("Gráficos")
        self.btn_graficos.clicked.connect(lambda: self.switch_page(1))

        self.btn_lista = QPushButton("Lista")
        self.btn_lista.clicked.connect(lambda: self.switch_page(2))

        # Layout da sidebar
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 40, 0, 0)
        self.sidebar_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.btn_dashboard, alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.btn_graficos)
        self.sidebar_layout.addWidget(self.btn_lista)
        self.sidebar_layout.addStretch()

        # 🔹 Adiciona espaçador antes da sidebar dentro do container
        self.sidebar_container.addItem(self.sidebar_spacer)
        self.sidebar_container.addWidget(self.sidebar)

        # Criando as páginas no QStackedWidget
        self.pages = QStackedWidget()
        self.pages.addWidget(Dashboard())  # Página do Dashboard
        self.pages.addWidget(self.create_graficos_page())  # Página de Gráficos
        self.pages.addWidget(self.create_lista_page())  # Página de Lista

        # 🔹 Adiciona container da sidebar e conteúdo ao layout principal
        self.main_layout.addLayout(self.sidebar_container)
        self.main_layout.addWidget(self.pages)

        # Configuração inicial para exibir a primeira página (Dashboard)
        self.pages.setCurrentIndex(0)

        # Animação para expandir/recolher
        self.animation = QPropertyAnimation(self.sidebar, QByteArray(b"minimumWidth"))
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    @staticmethod
    def create_dashboard_page():
        """Cria a página do Dashboard."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📊 Dashboard - Aqui ficam os KPIs"))
        return page

    @staticmethod
    def create_graficos_page():
        """Cria a página de Gráficos."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📈 Gráficos - Visualizações dos dados"))
        return page

    @staticmethod
    def create_lista_page():
        """Cria a página de Lista."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("📋 Lista - Informações detalhadas"))
        return page

    def switch_page(self, index):
        """Alterna entre as páginas no QStackedWidget."""
        self.pages.setCurrentIndex(index)

        # Reseta o estilo de todos os botões
        self.reset_buttons_style()

        # Aplica o estilo ao botão selecionado
        if index == 0:
            self.update_button_style(self.btn_dashboard)
        elif index == 1:
            self.update_button_style(self.btn_graficos)
        elif index == 2:
            self.update_button_style(self.btn_lista)

    def update_button_style(self, button):
        """Atualiza o estilo do botão clicado."""
        button.setStyleSheet("""
            background-color: #41AEF2;
            color: #FFFFFF;
            font-size: 18px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        """)
        # Atualiza o ícone (por exemplo)
        button.setIcon(QIcon(str(self.path_icons["home_black"])))

    def reset_buttons_style(self):
        """Reseta o estilo de todos os botões."""
        buttons = [self.btn_dashboard, self.btn_graficos, self.btn_lista]
        for button in buttons:
            button.setStyleSheet("""
                background-color: transparent;
                color: #000000;
                font-size: 18px;
                border-radius: 10px;
                box-shadow: none;
            """)
            button.setIcon(QIcon(str(self.path_icons["home_white"])))  # Ícone original (ou ícone padrão)

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
