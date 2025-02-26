from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QLineEdit, QAbstractButton


def password_setup(self) -> None:
    """
    Add QAction to QLineEdit to show password.

    :return: None
    """
    show_icon = QIcon()
    show_icon.addPixmap(QPixmap(":/show/view.png"), QIcon.Normal, QIcon.Off)

    action = QAction(self)
    action.setIcon(show_icon)
    self.pwdEdit.addAction(action, QLineEdit.TrailingPosition)

    show_pwd_button = self.pwdEdit.findChild(QAbstractButton)
    show_pwd_button.setCursor(Qt.PointingHandCursor)

    # Press to show and release to hide.
    show_pwd_button.pressed.connect(lambda: self.password_visibility(True))
    show_pwd_button.released.connect(lambda: self.password_visibility(False))
    self.pwdEdit.setClearButtonEnabled(True)

def password_visibility(self, show):
    if show:
        self.pwdEdit.setEchoMode(QLineEdit.Normal)
    else:
        self.pwdEdit.setEchoMode(QLineEdit.Password)
