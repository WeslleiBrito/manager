from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QFrame,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtGui import Qt, QPixmap, QImage
from PySide6.QtCore import QSize, QTimer
from pathlib import Path
from interfaces.home.home import Home

import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()

        # Pegando a localização do arquivo atual
        path_local = Path(__file__).parent

        # Configurando a janela
        self.setWindowTitle("Login")
        self.resize(QSize(400, 200))  # Nintendo o tamanho original da janela


        # Definindo o layout principal
        main_layout = QHBoxLayout()  # Layout horizontal para dividir a janela

        # Layout para os campos de entrada e botões (lado esquerdo)
        left_layout = QVBoxLayout()

        # Layout de usuário e senha
        input_layout = QVBoxLayout()
        label_user = QLabel("Usuário")
        self.combo_users = QComboBox()
        self.combo_users.addItems(["Wesllei", "Usuário 02"])
        self.combo_users.setMaximumWidth(200)  # Reduzindo a largura do combobox
        label_password = QLabel("Senha")
        self.line_text_password = QLineEdit()
        self.line_text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_text_password.setMaximumWidth(200)  # Reduzindo a largura do campo de senha

        # Adicionando widgets de input ao layout
        input_layout.addWidget(label_user)
        input_layout.addWidget(self.combo_users)
        input_layout.addWidget(label_password)
        input_layout.addWidget(self.line_text_password)

        # Layout de botões
        button_layout = QHBoxLayout()
        button_enter = QPushButton("Entrar")
        button_exit = QPushButton("Sair")
        button_enter.setMaximumWidth(90)  # Reduzindo a largura dos botões
        button_exit.setMaximumWidth(60)
        button_layout.addWidget(button_enter)
        button_layout.addWidget(button_exit)

        # Conectando os botões aos métodos
        button_enter.clicked.connect(self.on_enter_clicked)
        button_exit.clicked.connect(self.on_exit_clicked)

        # Adicionando os layouts de input e botões ao layout esquerdo
        left_layout.addLayout(input_layout)
        left_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        left_layout.addLayout(button_layout)

        # Adicionando um espaçador para empurrar os componentes para cima
        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Frame de logo (lado direito)
        logo_frame = QFrame()
        logo_layout = QVBoxLayout(logo_frame)

        # Carregando a imagem da logo
        logo_path = path_local / "../../src/logo.png"


        if not logo_path.exists():
            print(f"Erro: A imagem {logo_path} não foi encontrada.")
            sys.exit(1)

        img = QImage(str(logo_path)).scaled(
            150,
            150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        image_logo = QLabel()
        image_logo.setPixmap(QPixmap.fromImage(img))
        image_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adicionando espaçadores acima e abaixo da logo para centralizá-la verticalmente
        logo_layout.addWidget(image_logo)
        logo_layout.addSpacerItem(QSpacerItem(0, 40))


        # Adicionando os layouts esquerdo e direito ao layout principal
        main_layout.addLayout(left_layout)
        main_layout.addWidget(logo_frame)

        # Definindo o layout da janela
        self.setLayout(main_layout)


    def showEvent(self, event):
        """Centraliza a janela após ser exibida."""
        super().showEvent(event)

    def on_enter_clicked(self):
        user = self.combo_users.currentText()
        password = self.line_text_password.text()
        print(f"Usuário: {user}, Senha: {password}")
        # Adicione a lógica de autenticação aqui
        self.open_home()

    def on_exit_clicked(self):
        self.close()


    def open_home(self):
        self.window_home = Home()
        self.window_home.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Define um estilo consistente
    window = Login()
    window.show()
    sys.exit(app.exec())