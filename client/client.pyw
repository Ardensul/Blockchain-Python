## Python version check
import sys
if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    try:
        # Fallback TkInter error message box
        from tkinter import messagebox
        messagebox.showerror("Error", "This app requires Python 3.5 or newer to run.")
    except:
        # Fallback fallback console output
        print("ERROR: This app requires Python 3.5 or newer to run")

    sys.exit()

## Import Qt5
try:
    from PyQt5.QtWidgets import QApplication, QWidget                   # Generic Qt imports
    from PyQt5.QtWidgets import QLabel, QPushButton                     # User interaction imports
    from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout   # Layout imports
except:
    try:
        from tkinter import messagebox
        messagebox.showerror("Error", "This application requires PyQt5 to be installed on your system.")
    except:
        print("Error: This application requires PyQt5 to be installed on your system")

    sys.exit()

## Init app
app = QApplication([])          # Create application
window = QWidget()              # Define main window

## Define button action
sampleButton = QPushButton("Close")
sampleButton.clicked.connect(lambda:sys.exit())

## Define layout
grid = QGridLayout()
grid.addWidget(QLabel("Sample text and/or animation"), 0, 0)
grid.addWidget(sampleButton, 1, 0)

## Set layout and prime application to run
window.setLayout(grid)                  # Apply grid layout to window
window.setGeometry(100, 100, 200, 100)  # Set window geometry
window.setWindowTitle("Test")           # Set window title (...no really)
window.show()
sys.exit(app.exec_())

if __name__ == '__main__':
    window()
