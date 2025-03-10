import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QPushButton, QHBoxLayout, QLabel
from PySide6.QtCore import QPropertyAnimation, QBitArray
from PySide6.QtGui import Qt


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        self.expanded = True  # Estado inicial: expandido

        # Configuração do layout principal
        self.main_layout = QHBoxLayout(self)
        self.sidebar = QFrame()
        self.sidebar.setStyleSheet("background-color: #2c3e50; border-radius: 5px;")
        self.sidebar.setFixedWidth(200)  # Largura inicial expandida

        # Botão para expandir/recolher
        self.toggle_button = QPushButton("☰")
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.setStyleSheet("background-color: #34495e; color: white; border: none; font-size: 18px;")
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Layout do sidebar
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.addWidget(QLabel("Menu"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addStretch()

        # Layout da área de conteúdo
        self.content = QLabel("Conteúdo Principal")
        self.content.setStyleSheet("font-size: 24px; margin-left: 20px;")

        # Animação para expandir/recolher
        self.animation = QPropertyAnimation(self.sidebar)
        self.animation.setDuration(300)  # Duração da animação (ms)

        # Adiciona os widgets ao layout principal
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)

    def toggle_sidebar(self):
        """Expande ou retrai a sidebar com animação."""
        if self.expanded:
            self.animation.setStartValue(200)
            self.animation.setEndValue(50)
        else:
            self.animation.setStartValue(50)
            self.animation.setEndValue(200)

        self.animation.start()
        self.expanded = not self.expanded



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())