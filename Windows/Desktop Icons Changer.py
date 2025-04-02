from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QPushButton, QMainWindow, QMenuBar, QStatusBar, QWidget
import winreg
import sys
import subprocess

class Ui_MainWindow(object):
    REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel"
    ICONS = {
        "This PC": "{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
        "Network": "{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
        "User Folder": "{59031a47-3f72-44a7-89c5-5595fe6b30ee}",
        "Control Panel": "{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}"
    }

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        font = QFont()
        font.setPointSize(20)

        # Creazione delle etichette e checkbox
        self.labels = {}
        self.checkboxes = {}

        positions = [("This PC", 0), ("Network", 60), ("User Folder", 120), ("Control Panel", 180)]

        for name, y in positions:
            label = QLabel(name, self.centralwidget)
            label.setGeometry(QRect(20, y, 180, 50))
            label.setFont(font)
            self.labels[name] = label

            checkbox = QCheckBox("Enabled", self.centralwidget)
            checkbox.setGeometry(QRect(220, y, 171, 50))
            checkbox.setFont(font)
            checkbox.stateChanged.connect(lambda _, n=name: self.toggle_icon(n))
            self.checkboxes[name] = checkbox

        # Pulsante "Apply Changes"
        self.applyButton = QPushButton("Apply Changes", self.centralwidget)
        self.applyButton.setGeometry(QRect(140, 260, 180, 50))
        self.applyButton.setFont(font)
        self.applyButton.clicked.connect(self.restart_explorer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Imposta lo stato dei checkbox in base al registro
        self.check_icons_status()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Windows Icons Manager", None))

    def check_icons_status(self):
        """ Controlla lo stato delle icone leggendo i valori dal registro di sistema. """
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.REG_PATH) as key:
                for name, reg_value in self.ICONS.items():
                    try:
                        value, _ = winreg.QueryValueEx(key, reg_value)
                        self.checkboxes[name].setChecked(value == 0)  # 0 = visibile, 1 = nascosto
                    except FileNotFoundError:
                        self.checkboxes[name].setChecked(True)  # Assume che sia visibile se non esiste
        except FileNotFoundError:
            for name in self.ICONS:
                self.checkboxes[name].setChecked(True)  # Assume che siano visibili

    def toggle_icon(self, name):
        """ Aggiorna il registro per mostrare/nascondere l'icona corrispondente. """
        reg_value = self.ICONS[name]
        new_value = 0 if self.checkboxes[name].isChecked() else 1

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, reg_value, 0, winreg.REG_DWORD, new_value)
        except FileNotFoundError:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.REG_PATH) as key:
                winreg.SetValueEx(key, reg_value, 0, winreg.REG_DWORD, new_value)

    def restart_explorer(self):
        """ Riavvia Explorer per applicare le modifiche. """
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], shell=True)
        subprocess.run(["start", "explorer.exe"], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
