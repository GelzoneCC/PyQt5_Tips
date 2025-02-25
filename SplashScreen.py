# Add a startup screen while launching.

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from WindowControlle import MainWindowController

if __name__ = '__main__':
  app = QApplication([])
  # Add a splash screen before app startup.
  splash_pix = QPixmap(your_picture_path)
  splash_pix_fixed = splash_pix.scaled(600, 338)  # Adjust the size
  splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
  splash.setMask(splash_pix.mask())
  splash.show()
  window = MainWindowController()
  window.show()
  splash.finish(window)
  app.exec_()
