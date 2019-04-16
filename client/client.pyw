## Python version check
import sys
if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    try:
        # Fallback TkInter error message box
        from tkinter import messagebox
        messagebox.showerror("Error", "This app requires Python 3.5 or newer to run.")
    except:
        # Fallback fallback console output
        print("ERROR: This app requires Python 3.5 or newer to run.")

    sys.exit()

## Check dependencies
import dependencies
if dependencies.CheckDependencies() == False:
    sys.exit()

## Actually import functions after that
from PyQt5.QtWidgets import QApplication, QWidget                   # Generic Qt imports
from PyQt5.QtWidgets import QLabel, QPushButton                     # User interaction imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout   # Layout imports

## Import network functions
import network

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BisonDollar")

        # Label
        self.label = QLabel("Is miner running ?")

        # Button
        self.button = QPushButton("Check")
        self.button.clicked.connect(self.CheckIfMinerRunning)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.setLayout(self.layout)

        # Set window geometry
        self.setMinimumHeight(100)
        self.setMinimumWidth(200)
        
        # Show app
        self.show()

    # Very self-descriptive functions
    def CheckIfMinerRunning(self):
        if network.Ping7777() == True:
            self.label.setText("Miner is running")
        else:
            self.label.setText("Miner is not running")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    context = App()
    sys.exit(app.exec_())
