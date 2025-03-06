from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton
)

from PySide6.QtGui import (
    Qt,
    QPixmap,
    QImage
)

from PySide6.QtCore import (
    QSize
)

from pathlib import Path
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()

        # pegando a localização do arquivo atual
        path_local = Path(__file__).parent

        # Sentando a janela
        self.setWindowTitle("Login")
        self.resize(QSize(460, 280))

        # Definindo os containers
        main_container = QGridLayout()
        user_container = QVBoxLayout()
        logo_container = QVBoxLayout()
        button_container = QHBoxLayout()
        input_container_user = QVBoxLayout()
        input_container_password = QVBoxLayout()

        # Definindo os widgets
        user_widget = QWidget()
        label_user = QLabel("Usuário")
        combo_users = QComboBox()
        combo_users.addItems(["Wesllei", "Usuário 02"])
        label_password = QLabel("Senha")
        line_text_password = QLineEdit()
        line_text_password.setEchoMode(QLineEdit.EchoMode.Password)
        image_logo = QLabel()
        img = QImage(path_local / "../../src/logo.png").scaled(
            200,
            200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        image_logo.setPixmap(QPixmap.fromImage(img))
        image_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_enter = QPushButton("Entrar")
        button_exit = QPushButton("Sair")

        user_widget.setLayout(user_container)

        # Estilizando o container do usuário
        user_container.setSpacing(0)
        user_container.setContentsMargins(0, 0, 0 ,0)
        combo_users.setFixedSize(QSize(100, 20))
        line_text_password.setFixedSize(QSize(100, 20))

        # Estilizando os Botões
        button_enter.setFixedSize(100, 20)
        button_exit.setFixedSize(100, 20)

        # Adicionando os widgets aos seus respectivos container
        input_container_user.addWidget(label_user)
        input_container_user.addWidget(combo_users)
        input_container_password.addWidget(label_password)
        input_container_password.addWidget(line_text_password)

        user_container.addLayout(input_container_user)
        user_container.addLayout(input_container_password)
        logo_container.addWidget(image_logo)
        button_container.addWidget(button_enter)
        button_container.addWidget(button_exit)

        # Estilizando o container da main
        main_container.setColumnStretch(0, 2)
        main_container.setColumnStretch(1, 2)

        # Adicionado os containers a auxiliares ao container principal
        main_container.addWidget(user_widget, 0, 0, Qt.AlignmentFlag.AlignTop)
        main_container.addLayout(logo_container, 0, 1)
        main_container.addLayout(button_container, 1, 1)

        self.setLayout(main_container)


app = QApplication(sys.argv)
window = Login()
window.show()
sys.exit(app.exec())