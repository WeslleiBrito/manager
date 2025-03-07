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
    QSize,
    QTimer,
    QEvent
)

from pathlib import Path
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()

        # Pegando a localização do arquivo atual
        path_local = Path(__file__).parent

        # Configurando a janela
        self.setWindowTitle("Login")
        self.resize(QSize(460, 280))

        # Centraliza a janela após um pequeno delay
        QTimer.singleShot(500, self.center)

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
        self.combo_users = QComboBox()
        self.combo_users.addItems(["Wesllei", "Usuário 02"])
        label_password = QLabel("Senha")
        self.line_text_password = QLineEdit()
        self.line_text_password.setEchoMode(QLineEdit.EchoMode.Password)
        image_logo = QLabel()

        # Carregando a imagem da logo
        logo_path = path_local / "../../src/logo.png"
        if not logo_path.exists():
            print(f"Erro: A imagem {logo_path} não foi encontrada.")
            sys.exit(1)

        img = QImage(str(logo_path)).scaled(
            200,
            200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        image_logo.setPixmap(QPixmap.fromImage(img))
        image_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_enter = QPushButton("Entrar")
        button_exit = QPushButton("Sair")

        # Conectando os botões aos métodos
        button_enter.clicked.connect(self.on_enter_clicked)
        button_exit.clicked.connect(self.on_exit_clicked)

        user_widget.setLayout(user_container)

        # Estilizando o container do usuário
        user_container.setSpacing(0)
        user_container.setContentsMargins(0, 0, 0, 0)
        self.combo_users.setMinimumSize(100, 20)
        self.line_text_password.setMinimumSize(100, 20)

        # Estilizando os Botões
        button_enter.setMinimumSize(100, 20)
        button_exit.setMinimumSize(100, 20)

        # Adicionando os widgets aos seus respectivos containers
        input_container_user.addWidget(label_user)
        input_container_user.addWidget(self.combo_users)
        input_container_password.addWidget(label_password)
        input_container_password.addWidget(self.line_text_password)

        user_container.addLayout(input_container_user)
        user_container.addLayout(input_container_password)
        logo_container.addWidget(image_logo)
        button_container.addWidget(button_enter)
        button_container.addWidget(button_exit)

        # Estilizando o container principal
        main_container.setColumnStretch(0, 2)
        main_container.setColumnStretch(1, 2)

        # Adicionando os containers auxiliares ao container principal
        main_container.addWidget(user_widget, 0, 0, Qt.AlignmentFlag.AlignTop)
        main_container.addLayout(logo_container, 0, 1)
        main_container.addLayout(button_container, 1, 1)

        self.setLayout(main_container)

    def center(self):
        """Centraliza a janela na tela."""
        # Força a atualização da janela
        self.update()
        self.repaint()

        # Obtém a geometria da tela principal
        screen_geometry = QApplication.primaryScreen().geometry()

        # Calcula o centro da tela
        center_point = screen_geometry.center()

        # Obtém a geometria da janela
        window_geometry = self.frameGeometry()

        # Move a janela para o centro da tela
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

    def showEvent(self, event):
        """Centraliza a janela após ser exibida."""
        super().showEvent(event)
        self.center()

    def on_enter_clicked(self):
        user = self.combo_users.currentText()
        password = self.line_text_password.text()
        print(f"Usuário: {user}, Senha: {password}")
        # Adicione a lógica de autenticação aqui

    def on_exit_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Define um estilo consistente
    window = Login()
    window.show()
    sys.exit(app.exec())